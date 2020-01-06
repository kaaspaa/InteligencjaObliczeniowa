import pandas as pd
import numpy as np


def my_range(start, end, step):
    while start <= end:
        yield start
        start += step


def countOutput(arr1, arr2):
    val = 0
    for i in range(len(arr1)):
        for l in range(len(arr2)):
            val = val + (arr1[i][l] * arr2[i][l])
    return val


def function(array, layer):
    length = len(array)
    retArr = []
    for i in range(1, length-1): # od 1 do 6
        valArr = []
        for l in range(1, length-1):
            tempArr = []
            for k in range(-1, 2):
                tempArr.append([array[i+k][l-1], array[i+k][l], array[i+k][l+1]])
            valArr.append(countOutput(tempArr, layer))
        retArr.append(valArr)
    return retArr


def maxPooling(array):
    retArr = []
    for i in my_range(0, len(array)-1, 2):
        temp = []
        for l in my_range(0,len(array)-1, 2):
            temp.append(max(array[i][l], array[i][l+1], array[i+1][l], array[i+1][l+1]))
        retArr.append(temp)
    return retArr


df = pd.read_excel(r'deep1_8x8.xlsx')
picture = []
temp = [1, 0.7, 0.7, 1, 0.7, 0.7, 0.5, 0.2]
picture.append(temp)
for i in range(len(df.values)):
    picture.append(df.values[i].tolist())
layers = []
layers.append([[1, 0, -1],
               [1, 0, -1],
               [1, 0, -1]])
layers.append([[1, 1, 1],
               [0, 0, 0, ],
               [-1, -1, -1]])
layers.append([[1, 0, 0.5],
               [0, 0, 0],
               [0, -0.5, 0]])
layers.append([[1, 0, 1],
               [0, 1, 0],
               [1, 0, 1]])
arr1 = function(picture, layers[0])
arr2 = function(picture, layers[1])
print("arr1")
for i in arr1:
    print(i)
print("arr2")
for i in arr2:
   print(i)
arr1 = maxPooling(arr1)
arr2 = maxPooling(arr2)
print("arr1")
for i in arr1:
    print(i)
print("arr2")
for i in arr2:
    print(i)
arr1 = function(arr1, layers[2])
arr2 = function(arr2, layers[3])
print("arr1")
for i in arr1:
    print(i)
print("arr2")
for i in arr2:
    print(i)
final1 = arr1[0][0] * 0.5 + arr2[0][0] * 0.7
final2 = arr1[0][0] * 0.1 + arr2[0][0] * 0.2
print("final 1 = " + str(final1))
print("final 2 = " + str(final2))
