import numpy as np
from math import cos
def sigmoid(x):

  return 1 / (1 + np.exp(-x))

def invsigmoid(x):
 
  return 1-(1/ (3 + np.exp(-x)))

# Example usage
input_value =1
sigmoid_output1 = invsigmoid(3)
# sigmoid_output2 = invsigmoid(4)
sigmoid_output2 = invsigmoid(9)
sigmoid_output3 = invsigmoid(1)

# print(sigmoid_output1  * (cos(2)+cos(1)+cos(1)))
# print(sigmoid_output2 * (cos(2)+cos(4)+cos(3)+cos(2)))
# print(sigmoid_output3 * (cos(1)))

print(sigmoid_output1)
print(sigmoid_output2)
print(sigmoid_output3)