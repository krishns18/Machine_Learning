#!/usr/bin/python3

# Implementation of standardize data
from math import sqrt

# calculate column average
def column_average(data):
  averages = [0 for i in range(len(data[0]))]
  for i in range(len(data[0])):
    values = [item[i] for item in data]
    averages[i] = sum(values)/ float(len(data))
  return averages

# calculate standard deviation
def calculate_std(data,avg):
  std_devs = [0 for i in range(len(data[0]))]
  for i in range(len(data[0])):
    variance = [pow(item[i] - avg[i],2) for item in data]
    std_devs[i] = sum(variance)
  
  std_devs = [sqrt(item/(float(len(data)-1))) for item in std_devs]
  return std_devs

# standardize the data
def standardize(data,std,avg):
  for item in data:
    for i in range(len(item)):
      item[i] = (item[i] - avg[i])/std[i]
  
dataset = [[50, 30], [25,55], [20, 80], [40, 40]]

col_average = column_average(dataset)

std_dev = calculate_std(dataset,col_average)

standardize(dataset,std_dev,col_average)
print(dataset)
print("Column averages:",col_average)
print("Standard deviations:",std_dev)
print(dataset)

