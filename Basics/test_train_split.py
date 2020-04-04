#!/usr/bin/python3

# Implementation of test train split. default is 60-40 split
from random import seed
from random import randrange

seed(1)

def train_test_split(data,split=0.60):
  training_set = list()
  training_size = split * len(data)
  testing_set = list(data) # making a copy
  while len(training_set) < training_size:
    index = randrange(len(testing_set))
    training_set.append(testing_set.pop(index))

  return training_set,testing_set

dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
train, test = train_test_split(dataset)
print(train)
print(test)

