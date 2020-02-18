from collections import defaultdict
import csv
import random

listDict = dict()
with open('friends_list_or.csv', newline='') as csvfile:
     listfile = csv.reader(csvfile, delimiter=';')
     for row in listfile:
         tempSet = set()
         for i, element in enumerate(row):
            if i != 0:
                tempSet.add(element)
         listDict[row[0]] = tempSet



#This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self,vertices):
        self.V= vertices
        self.graph = defaultdict(set)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].add(v)

    # A function used by DFS
    def DFSUtil(self,v,visited, componentVertices):
        # Mark the current node as visited and print it
        visited[v]= True
        # print (v) #OLD
        componentVertices.add(v)

        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited, componentVertices)


    def fillOrder(self,v,visited, stack):
        # Mark the current node as visited
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph['{}'.format(v)]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)


    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g



    # The main function that finds and prints all strongly
    # connected components
    def printSCCs(self):
        componentVertices = set()
        numOfComponents = 0

        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited = dict.fromkeys(self.graph, False)
        # Fill vertices in stack according to their finishing
        # times
        for i in self.graph:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)

        # Create a reversed graph
        gr = self.getTranspose()

        # Mark all the vertices as not visited (For second DFS)
        # visited =[False]*(self.V)
        visited = dict.fromkeys(self.graph, False)

        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i]==False:
                gr.DFSUtil(i, visited, componentVertices)
               # print(componentVertices, " ---component size: ", len(componentVertices))
                print(" Сomponent size: ", len(componentVertices))
                #print("")
                numOfComponents += 1
                componentVertices.clear()
        print("Number of strongly connected components: ", numOfComponents)
# Create a graph given in the above diagram
g = Graph(len(listDict))
g.graph = listDict




print ("Following are strongly connected components " +
                           "in given graph")
g.printSCCs()


a = []
n = 1
for i in range (0,n):
    a.append(int(input()))
# m k
m = 0
for i in range (0,n):
    if (a[i] % 16 > 9 and a[i] >= 16*16 and a[i] < 16*16*16):
        m += a[i]
print(m)
