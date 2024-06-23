# There has to be an actual "Input.txt" file in project folder
with open("Input.txt", "r") as file:
    nodeAmount = int(file.readline())
    start, end = [int(num) for num in file.readline().split()]
    adj_matrix = [[int(num) for num in line.split()] for line in file]

from queue import Queue
def bfs(graph, start, end):
    frontier = Queue()
    frontier.put([start])
    explored = []
    while True:
        if frontier.empty():
            raise Exception("No way found Exception")
        path = frontier.get()      
        current_node = path[-1]
        #print(type(path), "Current path =", path)
        #print(type(current_node), "Current node =", current_node, '\n')
        explored.append(current_node)
        if current_node == end:
            print("Solution for BFS:", path)
            return
        i = -1
        for node in graph[current_node]:
            i = i + 1
            if (node == 1):
                if i not in explored:
                    new_path = list(path)
                    new_path.append(i)
                    frontier.put(new_path)

from queue import LifoQueue
def dfs(graph,start,end):
    frontier = LifoQueue()
    frontier.put([start])
    explored = []
    while True:
        if frontier.empty():
            raise Exception("No way found Exception")
        path = frontier.get()
        current_node = path[-1]
        #print(type(path), "Current path =", path)
        #print(type(current_node), "Current node =", current_node, '\n')
        explored.append(current_node)
        if current_node == end:
            print("Solution for DFS:", path)
            return
        i = 18
        for node in reversed(graph[current_node]):
            i = i - 1
            if (node == 1):
                if i not in explored:
                    new_path = list(path)
                    new_path.append(i)
                    frontier.put(new_path)

#bfs(adj_matrix, start, end)
#dfs(adj_matrix, start, end)

with open("InputUCS.txt", "r") as file:
    nodeAmount = int(file.readline())
    start, end = [int(num) for num in file.readline().split()]
    adj_matrix = [[int(num) for num in line.split()] for line in file]

from queue import PriorityQueue
def ucs(graph, start, end):
    frontier = PriorityQueue();
    frontier.put([0, [start]])  # (priority, node)
    explored = []
    while True:
        if frontier.empty():
                raise Exception("No way found")
        current_cost, path = frontier.get()
        current_node = path[-1]
        #print(type(current_cost), "Current cost =", current_cost)
        #print(type(path), "Current path =", path)
        #print(type(current_node), "Current node =", current_node, '\n')
        explored.append(current_node)
        if current_node == end:
            print("Solution for UCS:", path, "- Cost:", current_cost)
            return
        i = -1
        for cost in graph[current_node]:
            i = i + 1
            if (cost > 0):
                if i not in explored:
                    new_path = list(path)
                    new_path.append(i)
                    frontier.put([current_cost + cost, new_path])
        
#ucs(adj_matrix, start, end)
