# -*- Sustainability project -*-
"""
Created on Tue Jan  9 20:30:55 2018
@author: Aditya Linngam, Rishik Reddy
"""


#add dropdown with column names
import numpy as np
import matplotlib.pyplot as mplp
import pandas as pd

#datasetReader = []
count = 1
while(count != 5):
    print("data ",count, "/n")
    print("name of dataset including the suffix (example: MyDataset.csv)")
    datasetReader = pd.read_csv(input())
    print("name of column to read (example: AverageTempratures)")
    if(count == 1):
        data1 = datasetReader.loc[:,input()]
    if(count == 2):
        data2 = datasetReader.loc[:,input()]
    if(count == 3):
        data3 = datasetReader.loc[:,input()]
    if(count == 4):
        data4 = datasetReader.loc[:,input()]    
    count += 1
power = int(input("degree for regression 1 to 4 "))
xArray1 = []
xArray2 = []
xArray3 = []
xArray4 = []
count = 1
columnumbers = "d1y1" #not numbers names
#power1 = 2 del

length = len(data1)
for i in range(1, length + 1):
    xArray1.append(i)
length = len(data2)
for i in range(1, length + 1):
    xArray2.append(i)
length = len(data3)
for i in range(1, length + 1):
    xArray3.append(i)
length = len(data4)
for i in range(1, length + 1):
    xArray4.append(i)

'''
while(count != 5):
    start = 1
    Array = []
    print("the length of the dataset is equal to ", length)
    while(start != length + 1):
        xArray1 += [start]
        start = start +1
    if(count == 1): 
        xArray1 = Array
        length = len(data2)
    elif(count == 2):
        xArray2 = Array
        length = len(data3)
    elif(count == 3):
        xArray3 = Array
        length = len(data4)
    else:
        xArray4 = Array
    print(xArray1)
    count += 1
    '''
#d1y1 = dataset1.loc[:,'LandAverageTemperature']
#d1y2 = dataset1.loc[:,'LandMaxTemperature']
#d1y3 = dataset1.loc[:,'LandMinTemperature']
#d1y4 = dataset1.loc[:,'LandAndOceanAverageTemperature']
slope_data1 = np.polyfit(xArray1,data1,power)
slope_data2 = np.polyfit(xArray1,data2,power)
slope_data3 = np.polyfit(xArray1,data3,power)
slope_data4 = np.polyfit(xArray1,data4,power)
print(slope_data1)
print(slope_data2)
print(slope_data3)
print(slope_data4)
#numX = 0
#columns = []
count = 1
#arrayName = xArray1
#plotX = []
#a = 1

while(count != 5):
    if(count == 1):
        xForAll = xArray1
        yForAll = data1
        slopeForAll = slope_data1
    elif(count == 2):
        xForAll = xArray2
        yForAll = data2
        slopeForAll = slope_data2
    elif(count == 3):
        xForAll = xArray3
        yForAll = data3
        slopeForAll = slope_data3
    else:
        xForAll = xArray4
        yForAll = data4
        slopeForAll = slope_data4        
    mplp.figure(count)
    mplp.plot(xForAll, yForAll, "o")
    mplp.plot(xForAll, np.polyval(slopeForAll, xForAll), "r--")
    count += 1

'''
while(columnumbers != "end"):
    print("what are the colum numbers for graph ", count)
    columnumbers = str(input())
    if(columnumbers=="1"or columnumbers=="2"or columnumbers=="3"or columnumbers=="4"):
        if(columnumbers == "1"):
            columns += d1y1          
        elif(columnumbers == "2"):
            columns += d1y2
        elif(columnumbers == "3"):
            columns += d1y3
        elif(columnumbers == "4"):
           columns += d1y4
        arrayName = xArray1
    else:
        print("eror")
        count -= 1
        numX -= 1
    numX += 1
while(a != numX):
    plotX += arrayName
    a += 1
mplp.plot(plotX, columns,"o")
'''
