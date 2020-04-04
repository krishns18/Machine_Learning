#!/usr/bin/python3

# K-fold validation implementation

from random import seed
from random import randrange

def cross_validation_split(data,folds=5):
  splits = list()
  data_copy = list(data)
  fold_size = int(len(data)/folds)
  
  for i in range(folds):
    fold = list()
    while len(fold) < fold_size:
      index = randrange(len(data_copy))
      fold.append(data_copy.pop(index))
    splits.append(fold)

  return splits


seed(1)
dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
folds = cross_validation_split(dataset, 5)
print(folds)
  

