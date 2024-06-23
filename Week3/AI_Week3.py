with open("Map.txt") as file:   
    h = [];
    for num in file.readline().split():
        h.append(int(num))
    adj_matrix = [[int(num) for num in line.split()] for line in file]

from queue import PriorityQueue
def aStar(start, end, heu, graph):
    frontier = PriorityQueue()
    frontier.put([0, [0, [start]]])
    explored = []
    while True:
        if frontier.empty():
            raise Exception("No way found")
        f_value, cost_and_path = frontier.get()
        move_cost, path = cost_and_path
        #print(type(path), "Current path:", path)
        #print(type(move_cost), "Current cost:", move_cost)
        #print(type(f_value), "Current cost + heuristic:", f_value, '\n')
        current = path[-1]
        explored.append(current)
        if current == end:
            name = ["Arad", "Zerind", "Oradea", "Timisoara", "Lugoj", "Mehadia", "Drobeta",
                    "Craiova", "Sibiu","Rimnicu Vilcea", "Pitesti", "Fagaras", "Bucharest",
                    "Giurgiu", "Urziceni", "Hirsova", "Eforie", "Vaslui", "Iasi", "Nearmt"]
            for i in range(len(path)):
                change = path[i]
                path[i] = name[change]
            print("Solution for A* search:\n", path, "\nCost:", move_cost)
            return
        i = -1
        for cost in graph[current]:
            i = i + 1
            if cost > 0:
                if i not in explored:
                    new_path = list(path)
                    new_path.append(i)
                    frontier.put([move_cost + cost + heu[i], [move_cost + cost, new_path]])

aStar(0, 15, h, adj_matrix)

#    openset = set()
#    closeset = set()

#    current = start

#    openset.add(current)
#    # While the open set is not empty
#    while openset:
#        # Find the item with the lowest G + H score
#        current = min(openset, key = lambda o:o.G + o.H)

#        if current == goal:
#            path = []
#            while current.parent:
#                path.append(current)
#                current = current.parent
#            path.append(current)
#            return path[::-1]
#        openset.remove(current)
#        closeset.add(current)
#        # Loop through the node's children
#        for node in children(current, grid):
#            # If it is already in the close set, skip it
#            if node in closeset:
#                continue
#            # If it is already in the open set, then
#            if node in openset:
#                # Check if new G score beats old G score
#                new_g = current.G + current.move_cost(node)
#                if node.G > new_g:
#                    node.G = new_g
#                    node.parent = current
#            else:
#                node.G = current.G + current.move_cost(node)
#                node.H = manhattan(node, goal)
#                node.parent = current
#                openset.add(node)
#    # Throw an exception if there is no path
#    raise Exception("No way found")

#def next_move(pacman, food, grid):
#    # Convert all the point to instances of node
#    for x in xrange(len(grid)):
#        for y in yrange(len(grid[x])):
#            grid[x][y] = Node(grid[x][y], (x, y))
#    # Get the path
#    path = aStar(grid[pacman[0]][pacman[1]], grid[food[0]][food[1]], grid)
#    # Output the path
#    print(len(path) - 1)
#    for node in path:
#        x, y = node.point
#        print(x, y)
