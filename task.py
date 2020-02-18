import numpy as np
import csv
import random

listDict = dict()
with open('friends_list_unor.csv', newline='') as csvfile:
     listfile = csv.reader(csvfile, delimiter=';')
     for row in listfile:
         tempSet = set()
         for i, element in enumerate(row):
            if i != 0:
                tempSet.add(element)
         listDict[row[0]] = tempSet



def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

#MAIN

#EXPORTING LARGEST COMPONENT
EXPORT = set()
#

totalVertices = 0
maxComponent = 0
notVisited=set(listDict.keys())
while len(notVisited) > 0:
    start = next(iter(notVisited))
    visited = dfs(listDict, start)
    notVisited -= visited

    #EXPORTING LARGEST COMPONENT

    print('Component size: ', len(visited))
    totalVertices += len(visited)
    if(len(visited) > maxComponent):
        maxComponent = len(visited)
    if len(visited) == maxComponent:
        EXPORT = visited
print('Largest component: ', maxComponent, '; ', maxComponent/totalVertices)

#EXPORTING LARGEST COMPONENT

import csv
with open('exported.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for el in EXPORT:
        row = [el]
        row.extend(listDict[el])
        csvwriter.writerow(row)
        row = []


n = int(input())
a = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)


a = []
n = 6
for i in range (0,n):
    a.append(int(input()))
j = 0
k = 0
m = 0
for i in range(0,n):
    if (a[i] % 2 == 0):
        j += 1
    else:
        k += 1
if ( j >= k):
    for i in range (0,n):
        if (a[i] % 2 == 0 and a[i] > m):
            m = a[i]
else:
    for i in range (0, n):
        if (a[i] % 2 != 0 and a[i] > m):
            m = a[i]
print(m,j,k)



a = []
n = 6
for i in range (0,n):
    a.append(int(input()))
j = 0
k = 0
m = 0
for i in range(0,n):
   if (a[i] % 2 == 0):
       j +=1
       if (a[i] > k):
           k = a[i]
   else:
       j -= 1
       if (a[i] > m):
           m = a[i]
if (j >= 0):
    print (k)
else:
    print (m)



a = []
n = 6
for i in range (0,n):
    a.append(int(input()))
max = 0
for i in range(0,n):
    if (a[i] % 3 != 0 and a[i] > 9 and a[i] < 100 and a[i] > max):
        max = a[i]
if (max !=0):
    print(max)
else:
    print('не найдено')



a = []
n = 6
for i in range (0,n):
    a.append(int(input()))
min = 1000
for i in range(0,n):
    if (a[i] % 7 == 0 and a[i] > 99 and a[i] < 1000 and a[i] < min):
        min = a[i]
if (min != 1000):
    print(min)
else:
    print('не найдено')



a = []
n = 6
for i in range (0,n):
    a.append(int(input()))
min = -1
for i in range(0,n):
    if (a[i] > 0 and (min == -1 or a[i] < min)):
        min = a[i]
if (min != -1):
    print(min)
else:
    print('не найдено')


a = []
n = 6
for i in range (0,n):
    a.append(int(input()))
k = 0
for i in range(0,n-1):
    if ( (a[i] + a[i+1])%2 == 0 and (a[i]+a[i+1])%4 != 0):
        k += 1
print (k)



a = []
n = 6
for i in range (0,n):
    a.append(int(input()))
k = 0
for i in range(0,n-1):
    if ( (a[i] + a[i+1])%2 == 0 and (a[i]+a[i+1])%4 != 0):
        k += 1
print (k)
