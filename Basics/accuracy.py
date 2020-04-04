#!/usr/bin/python3

# accuracy metric

def accuracy(actual,predicted):
  if len(actual) != len(predicted):
    print("length of actual and predicted values does not match")

  correct_predictions = 0
  for i in range(len(actual)):
    if actual[i] == predicted[i]:
      correct_predictions += 1

  return correct_predictions/len(actual) * 100

actual = [0,0,0,0,0,1,1,1,1,1]
predicted = [0,1,0,0,0,1,0,1,1,1]
result = accuracy(actual, predicted)
print(result)
