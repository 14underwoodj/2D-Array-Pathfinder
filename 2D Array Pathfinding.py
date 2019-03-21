import random
import math

class Node:
    value = 0
    visited = False
    distance = math.inf
    predecessor = 0,0

    def __init__(self, v):
        self.value = v

map = []

sizeY = 59 #79 #59
sizeX = 79 #126 #79

startPoint = (0,0)
finishPoint = (sizeY-1,sizeX-1)

for y in range(0,sizeY):
    map.append([])
    for x in range(0,sizeX):
        map[y].append(0)

def createMap():
    toPrint = ""
    for y in range(0,sizeY):
        for x in range(0,sizeX):
            map[y][x] = Node(random.randint(10, 99))
            toPrint += str(map[y][x].value) + " "
        toPrint += "\n"

    print(toPrint)

def printDistanceMap():
    toPrint = ""
    for y in range(0,sizeY):
        for x in range(0,sizeX):
            toPrint += str(map[y][x].distance) + " "
        toPrint += "\n"
    print(toPrint)

def printSolution(y, x):
    solution = []
    while True:
        solution.append((y,x))
        y = map[y][x].predecessor[0]
        x = map[y][x].predecessor[1]
        if(x == 0 and y == 0):
            break
    solution.append(startPoint)
    #print(solution)

    toPrint = ""
    for y in range(0,sizeY):
        for x in range(0,sizeX):
            
            if((y,x) in solution):
                toPrint += "   "
            else:
                toPrint += str(map[y][x].value) + " "
        toPrint += "\n"
    print(toPrint)

def findNextShortestNode():
    shortestDistance = math.inf
    shortestNode = 0,0
    for y in range(0,sizeY):
        for x in range(0,sizeX):
            if(map[y][x].distance < shortestDistance and map[y][x].visited == False):
                shortestDistance = map[y][x].distance
                shortestNode = y,x
    global done
    if(shortestDistance == math.inf):
        done = True
    return shortestNode


createMap()

done = False

map[startPoint[0]][startPoint[1]].distance = map[startPoint[0]][startPoint[1]].value

while done == False:
    nextShortestNode = findNextShortestNode()
    y = nextShortestNode[0]
    x = nextShortestNode[1]

    if(x-1 >= 0 and map[y][x-1].visited == False):
        map[y][x-1].distance = map[y][x].distance + map[y][x-1].value
        map[y][x-1].predecessor = y,x

    if(x+1 < len(map[y]) and map[y][x+1].visited == False):
        map[y][x+1].distance = map[y][x].distance + map[y][x+1].value
        map[y][x+1].predecessor = y,x

    if(y-1 >= 0 and map[y-1][x].visited == False):
        map[y-1][x].distance = map[y][x].distance + map[y-1][x].value
        map[y-1][x].predecessor = y,x
       
    if(y+1 < len(map) and map[y+1][x].visited == False):
        map[y+1][x].distance = map[y][x].distance + map[y+1][x].value
        map[y+1][x].predecessor = y,x

    map[y][x].visited = True

#printDistanceMap()

toSolution = input("Enter solution coordinates or press enter: ")

if(toSolution == ""):
    printSolution(finishPoint[0], finishPoint[1])
else:
    printSolution(int(toSolution.split(",")[0]), int(toSolution.split(",")[1]))








