import csv

#read from kiwiData.csv
file = open('C:/Users/jerem/Desktop/Dev/2021/Python/KiwiSorting/kiwiData.csv', 'r') #open csv in read mode
csvReader = csv.reader(file, delimiter = ',')
csvList = list(csvReader) #creates list out of csv
file.close()


'''
#bubble sort function
def bubbleSort(listName, sortIndex):
    n = len(listName)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if(listName[j][sortIndex] > listName[j + 1][sortIndex]):
                listName[j], listName[j + 1] = listName[j + 1], listName[j]

bubbleSort(csvList, 2)
'''


#selection sort function
def selectionSort(listName, sortIndex):
    n = len(listName)
    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if(listName[minimum][sortIndex] > listName[j][sortIndex]):
                minimum = j
                listName[i], listName[minimum] = listName[minimum], listName[i]

selectionSort(csvList, 2)

#write into sorted csv
file = open('C:/Users/jerem/Desktop/Dev/2021/Python/KiwiSorting/sortedKiwiData.csv', 'w') #open csv in write mode

for i in csvList[-1]: #writes column names
    file.write(i + ',')
file.write('\n')

n = len(csvList)
o = len(csvList[0])
for i in range(n - 1): #writes kiwi data
    for j in range(o):
        file.write(csvList[i][j] + ',')
    file.write('\n')