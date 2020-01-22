#!/usr/bin/python3

from csv import reader

from csv import reader

def load_csv(filename):
  dataset = list()
  with open(filename,'r') as file:
    csv_reader = reader(file)
    for row in csv_reader:
      if not row:
        continue
      dataset.append(row)
  return dataset

def convert_column_to_float(dataset,column):
  for row in dataset:
    row[column] = float(row[column].strip())

def dataset_minmax(dataset):
  minmax = list()
  for i in range(len(dataset[0])):
    col_values = [row[i] for row in dataset]
    value_min = min(col_values)
    value_max = max(col_values)
    minmax.append([value_min,value_max])

  return minmax

def normalize_dataset(dataset,minmax):
  for row in dataset:
    for i in range(len(row)):
      row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

dataset = load_csv('pima-indians-diabetes.csv')

for i in range(len(dataset[0])):
  convert_column_to_float(dataset, i)

minmax = dataset_minmax(dataset)
normalize_dataset(dataset,minmax)

print(dataset[0])
