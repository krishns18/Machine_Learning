#!/usr/bin/python3

# Example to normalize data
# Here we are rescaling an input to range between 0 and 1.

def getMinMax(data):
  minMax = list()
  for i in range(len(data[0])):
    col = [item[i] for item in data]
    minVal = min(col)
    maxVal = max(col)
    
    minMax.append([minVal,maxVal])

  return minMax

# normalize dataset
def normalize(data,minmax):
  for item in data:
    for i in range(len(item)):
      item[i] = (item[i] - minmax[i][0])/(minmax[i][1] - minmax[i][0])

dataset = [[20, 30], [40, 60], [90,50]]

print("Original dataset: {}".format(dataset))

minMaxVal = getMinMax(dataset)
normalize(dataset,minMaxVal)
print("Normalized dataset: {}".format(dataset))


