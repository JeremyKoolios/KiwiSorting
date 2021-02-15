import csv
import time
import matplotlib.pyplot as mathPlot

#read from kiwiData.csv
file = open('C:/Users/jerem/Desktop/Dev/2021/Python/KiwiSorting/kiwiData.csv', 'r') #open csv in read mode
csvReader = csv.reader(file, delimiter = ',')
csvList = list(csvReader) #creates list out of csv
file.close()



#bubble sort function
def bubbleSort(listName, sortIndex):
    n = len(listName)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if(listName[j][sortIndex] > listName[j + 1][sortIndex]):
                listName[j], listName[j + 1] = listName[j + 1], listName[j]


#selection sort function
def selectionSort(listName, sortIndex):
    n = len(listName)

    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if(listName[minimum][sortIndex] > listName[j][sortIndex]):
                minimum = j
            listName[i], listName[minimum] = listName[minimum], listName[i]


#sort and time
timeStart = time.time()
selectionSort(csvList, 2)
timeEnd = time.time()
print('Time taken:', timeEnd - timeStart)


#write into sorted csv
file = open('C:/Users/jerem/Desktop/Dev/2021/Python/KiwiSorting/sortedKiwiData.csv', 'w') #open csv in write mode

for i in csvList[-1]: #writes column names
    file.write(i + ',')
file.write('\n')

for i in range(len(csvList) - 1): #writes kiwi data
    for j in range(len(csvList[0])):
        file.write(csvList[i][j] + ',')
    file.write('\n')



#plot
height = []
weight = []

for i in range(len(csvList) - 1): #gets height and weight data
    height.append(float(csvList[i][3]))
    weight.append(float(csvList[i][2]))


mathPlot.scatter(height, weight, s=10) #creates the graph
mathPlot.xlim(33, 53)
mathPlot.ylim(0, 4.5)
mathPlot.xlabel('Height(cm)')
mathPlot.ylabel('Weight(kg)')
mathPlot.grid()
mathPlot.title('Kiwi Data')

mathPlot.show()
