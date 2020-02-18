import csv
import numpy as np

listDict = dict()
with open('exported.csv', newline='') as csvfile:
     listfile = csv.reader(csvfile, delimiter=';')
     for row in listfile:
         tempSet = set()
         for i, element in enumerate(row):
            if i != 0:
                tempSet.add(element)
         listDict[row[0]] = tempSet


#sumOfDegrees = 0
degrees = []
for el in listDict:
    degree =[el, len(listDict[el])]
    degrees.append(degree)
 #   sumOfDegrees += degree

#print('Average vertex degree: ', sumOfDegrees/228)


#degreeCount = {a+1: 0 for a in range(max(degrees))}
#for d in degrees:
 #   degreeCount[d] += 1

#for d in degreeCount:
 #   print(d, ':', degreeCount[d])

#with open('histogram.csv', 'w', newline='') as csvfile:
 #   csvwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  #  csvwriter.writerow(degreeCount.keys())
   # csvwriter.writerow(degreeCount.values())

#################################

shortestPaths = {}

def bfs(graph, start):
    visited, q1,q2, d, paths = set(), [start],[],0, []
    while q1 or q2:
        if (d%2 == 0):
            while q1:
                vertex = q1.pop(0)
                if vertex not in visited:
                    visited.add(vertex)
                    q2.extend(graph[vertex] - visited)
                    paths.append(d)
            d += 1


        else:
            while q2:
                vertex = q2.pop(0)
                if vertex not in visited:
                    visited.add(vertex)
                    q1.extend(graph[vertex] - visited)
                    paths.append(d)
            d += 1
    return paths

closenesscentrality =[]
for i, el in enumerate(listDict):
    res = bfs(listDict,el)
    closenesscentrality.append((227)/sum(res))


radius, diameter, mylist ,avg, closenesscentrality = 228,0,[], 0,[]
for i, el in enumerate(listDict):
    res = bfs(listDict,el)
    avg += sum(res)/(len(res)-1)
    closenesscentrality.append((227)/sum(res))
    mylist.append([el, max(res)])
    if max(res) > diameter:
        diameter = max(res)
    if max(res) < radius:
        radius = max(res)




central, peripheral = [],[]
for row in mylist:
    if row[1] == radius:
        central.append(row[0])
    elif row[1] == diameter:
        peripheral.append(row[0])

print('Radius: ', radius,'  Diameter', diameter)
print('Central vertex: ', central)
print('Peripheral vertex: ',peripheral)
print('Average: ', avg/228)


#########################TASK3
#########################CommonNeighbors

n = len(listDict)+1
CommonNeighbors = [[0] * n for i in range(n)]
for i,el in enumerate(listDict):
    CommonNeighbors[0][i+1] = el
    CommonNeighbors[i+1][0] = el
for i,x in enumerate(listDict):
    for j,y in enumerate(listDict):
        CommonNeighbors[i+1][j+1] = len(listDict[x]&listDict[y])

import csv
with open('CommonNeighbors.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in CommonNeighbors:
        csvwriter.writerow(row)

###################################Jaccard’s Coefficient

n = len(listDict)+1
JaccardsCoef = [[0] * n for i in range(n)]
for i,el in enumerate(listDict):
    JaccardsCoef[0][i+1] = el
    JaccardsCoef[i+1][0] = el
for i,x in enumerate(listDict):
    for j,y in enumerate(listDict):
        JaccardsCoef[i+1][j+1] = len(listDict[x]&listDict[y])/len(listDict[x]|listDict[y])

import csv
with open('JaccardsCoef.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in JaccardsCoef:
        csvwriter.writerow(row)


n = len(listDict)+1
AdamicAdar = [[0] * n for i in range(n)]
for i,el in enumerate(listDict):
    AdamicAdar[0][i+1] = el
    AdamicAdar[i+1][0] = el
for i,x in enumerate(listDict):
    for j,y in enumerate(listDict):
        sum = 0
        for el in listDict[x]&listDict[y]:
            if(len(listDict[el])):
                sum += 1/np.log(len(listDict[el]))
        AdamicAdar[i + 1][j + 1] = sum

import csv
with open('AdamicAdar.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in AdamicAdar:
        csvwriter.writerow(row)

n = len(listDict)+1
PreferentialAttachment = [[0] * n for i in range(n)]
for i,el in enumerate(listDict):
    PreferentialAttachment[0][i+1] = el
    PreferentialAttachment[i+1][0] = el
for i,x in enumerate(listDict):
    for j,y in enumerate(listDict):
        PreferentialAttachment[i + 1][j + 1] = len(listDict[x])*len(listDict[y])

import csv
with open('PreferentialAttachment.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in PreferentialAttachment:
        csvwriter.writerow(row)

#####################################TASK4
#################degree centrality

degreecentrality = []
for el in degrees:
   degreecentrality.append(el[1] / 227)
print('degree centrality',degreecentrality)
print('closeness centrality', closenesscentrality)

matrix = np.genfromtxt('exported_matrix.csv', delimiter=';', dtype='int')
x = np.linalg.eig(matrix)[1][:,np.linalg.eig(matrix)[0].argmax(axis=0)].real


    #for row in closenesscentrality:
     #   csvwriter.writerow(row)
    #csvwriter.writerow(x)
    #for el in Centrality:
      #  csvwriter.writerow(el)


#eigen centrality

degreeCentrality = {}
for i, el in enumerate(listDict):
    degreeCentrality[el] = degreecentrality[i]

closenessCentrality = {}
for i, el in enumerate(listDict):
    closenessCentrality[el] = closenesscentrality[i]

matrix = np.genfromtxt('exported_lbl.csv', delimiter=';', dtype='int')
matrix_not_labeled = np.genfromtxt('exported_wo_lbl.csv', delimiter=';', dtype='int')

eig = np.linalg.eig(matrix_not_labeled)[1][:,np.linalg.eig(matrix)[0].argmax(axis=0)].real
print('EIGEN: ')
# print(eig)

eigenCentrality = {}
for i, el in enumerate(matrix[0][1:229]):
    if i != 0:
        eigenCentrality[el] = eig[i]
print(eigenCentrality)
with open('centrality_res.csv', 'w', newline='') as c_csvfile:
    csvwriter = csv.writer(c_csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(['Id', 'degree_centrality', 'closeness_centrality', 'eigen_centrality'])
    for el in enumerate(listDict):
        csvwriter.writerow([el,  eigenCentrality[el]])

