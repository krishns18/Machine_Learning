#!/usr/bin/python3

from csv import reader

filename='../datasets/admissions.csv'

def basic_load_csv(f):
  file = open(f,'r')
  all_lines = reader(file)
  data = list(all_lines) # return the list
  return data

dataset = basic_load_csv(filename)
print("Total items in file: {} are:{}".format(filename,len(dataset)))

# optimized loading method. We can use it to ignore header and missing lines.

def optimized_load_csv(f):
  data = list()
  with open(f,'r') as file:
    csvfile = reader(file)
    next(csvfile) # skip the header row.
    for row in csvfile:
      if not row:
        continue # skip empty lines
      data.append(row)

  return data

dataset = optimized_load_csv(filename)
print("Total items in file: {} are:{}".format(filename,len(dataset)))
