class Node:
    goal_state = [0,0,0]
    def __init__(self, state, parent, action, depth):
        self.parent = parent
        self.state = state
        self.action = action
        self.depth = depth

    def __str__(self):
        return str(self.state)

    def goal_test(self):
        if self.state == self.goal_state:
            return True
        return False

    def is_valid(self):
        missionaries = self.state[0]
        cannibals = self.state[1]
        boat = self.state[2]
        if missionaries < 0 or missionaries > 3:
            return False
        if cannibals < 0 or cannibals > 3:
            return False
        if boat < 0 or boat > 1:
            return False
        return True

    def is_killed(self):
        missionaries = self.state[0]
        cannibals = self.state[1]
        if missionaries < cannibals and missionaries > 0:
            return True
        # Check for other side
        if missionaries > cannibals and missionaries < 3:
            return True
        ## [3,0,x] and [0,3,x] case, no hope
        #if (missionaries == 3 and cannibals == 0) or (missionaries == 0 and cannibals == 3):
        #    return True

    def generate_child(self):
        children = []
        depth = self.depth + 1 

        # Check if self is wrong
        if(not self.is_valid() or self.is_killed()):
            print(self.state, "This Input State Is Wrong!")
            return children
        
        if self.state[2] == 0:
            new_state = self.state.copy()
            new_state[2] = new_state[2] + 1
            action = [0,0,1]
            new_node = Node(new_state, self, action, depth)
            children.append(new_node)
        if self.state[2] == 1:
            for x in range(3):
                for y in range(3):
                    new_state = self.state.copy()
                    new_state[0] = new_state[0] - x
                    new_state[1] = new_state[1] - y
                    new_state[2] = new_state[2] - 1
                    action = [-x,-y,-1]
                    new_node  = Node(new_state, self, action, depth)
                    if (new_node.is_valid() and not new_node.is_killed()):
                        if x + y >= 1 and x + y <= 2:
                            children.append(new_node)
        return children

    def find_solution(self):
        path = []
        solution = []
        node = self
        while node.parent != None:            
            path.append(node.state)
            solution.append(node.action)
            node = node.parent

        # The while loop above will miss the last node, which is the starting node,
        # we need to manually add its state and action into path and solution
        path.append(node.state)
        solution.append(node.action)
        
        ## The last node, which is the starting node, whose action value is None,
        ## the following code is to remove the last value from list.
        ## However, it is okay not to remove it
        #solution = solution[:-1]
        
        path.reverse()
        solution.reverse()
        return path, solution

from queue import LifoQueue
def dfs():
    start = Node([3,3,1], None, None, 0)
    frontier = LifoQueue()
    frontier.put(start)
    while True:
        if frontier.empty():
            raise Exception("No solution found")

        current_node = frontier.get()
        print(current_node)
        if (current_node.goal_test()):            
            print("Path:", current_node.find_solution()[0])
            print("Action:", current_node.find_solution()[1])
            return
        else:
            num = len(current_node.generate_child())
            for i in range(num):
                frontier.put(current_node.generate_child()[i])

dfs()

#node = Node([3,3,1], None, None, 0)
#for i in range(len(node.generate_child())):
#    print(node.generate_child()[i])

#queue = [[1,2,3], [4,5,6], [7,8,9]]
#queue = queue[:-1]
#print(queue, len(queue))
