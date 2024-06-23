with open("Input.txt") as file:
    line1 = file.readline().split()
    ShapeAmount = int(line1[0])
    start = (int(line1[1]), int(line1[2]), 0)
    goal = (int(line1[3]), int(line1[4]), 9)
    heuristic = [float(num) for num in file.readline().split()]
    graph = []
    for x in range(ShapeAmount + 1):
        shape = []
        line = file.readline().split()
        vertices = int(line[0])
        for i in range(vertices):
            location = (int(line[i * 2 + 1]), int(line[i * 2 + 2]), x + 1)
            shape.append(location)
        graph.append(shape)

def line_func(ver1, ver2):
    if (ver1[0] == ver2[0]):
        a = 1; b = 0; c = -ver1[0]
    elif (ver1[1] == ver2[1]):
        a = 0; b = 1; c = -ver1[1]
    else:
        a = ver1[1] - ver2[1]
        b = ver2[0] - ver1[0]
        c = - ver1[0] * a - ver1[1] * b
    return a, b, c

def line_check(d, ver1, ver2):
    first = d[0] * ver1[0] + d[1] * ver1[1] + d[2]
    second = d[0] * ver2[0] + d[1] * ver2[1] + d[2]
    return first * second

def visible_vertice(d1, d2, d3, current, ver1, ver2, vertice):
    first = line_check(d1, vertice, ver2)
    second = line_check(d2, vertice, ver1)
    third = line_check(d3, vertice, current)
    if first >= 0 and second >= 0 and third < 0:
        return False
    return True

import math
from queue import PriorityQueue
def find_way_aStar(start, goal, graph, heu):
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
        if current == goal:
            solution = ""
            for node in path[0:-1]:
                solution += str(node) + " --> "
            solution += str(path[-1])
            print("Solution:", solution)
            print("Cost:", move_cost)
            return
        invisible = set()
        for shape in graph:
            for i in range(len(shape)):
                if i == len(shape) - 1:
                    ver1 = shape[i]
                    ver2 = shape[0]
                else:
                    ver1 = shape[i]
                    ver2 = shape[i + 1]            
                d1 = line_func(current, ver1)
                d2 = line_func(current, ver2)
                d3 = line_func(ver1, ver2)
                for shape2 in graph:
                    for vertice in shape2:
                        if vertice not in explored:
                            if not visible_vertice(d1, d2, d3, current, ver1, ver2, vertice):
                                invisible.add(vertice)
        count = -1
        for shape in graph:
            count = count + 1
            for vertice in shape:
                if vertice not in explored and vertice not in invisible:
                    new_path = list(path)                            
                    new_path.append(vertice)
                    cost = math.sqrt((current[0] - vertice[0]) ** 2 + (current[1] - vertice[1]) ** 2)
                    frontier.put([move_cost + cost + heu[count], [move_cost + cost, new_path]])
    
                
find_way_aStar(start, goal, graph, heuristic)
