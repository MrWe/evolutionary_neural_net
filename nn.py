import numpy as np
import random
import math

class NN(object):
  """docstring for NN."""
  def __init__(self, input_size, hidden_size, output_size):
    self.input_size = input_size + 1 #+1 for bias
    self.hidden_size = hidden_size
    self.output_size = output_size

    self.ai = [1.0] * self.input_size
    self.ah = [1.0] * self.hidden_size
    self.ao = [1.0] * self.output_size

  def set_NN_weights(self, input_weights, output_weights):
    self.wi = np.random.randn(self.input_size, self.hidden_size)
    self.wo = np.random.randn(self.hidden_size, self.output_size)

  def set_random_NN_weights(self):
    self.wi = np.multiply(np.random.randn(self.input_size, self.hidden_size),10)

    self.wo = np.multiply(np.random.randn(self.hidden_size, self.output_size), 10)

  def construct_init_nn(self, input_size, hidden_size, output_size):
    for i in range(input_size):
      self.input_weights.append([])
      for j in range(hidden_size):
        self.input_weights[i].append(random.uniform(-.5, .5))
    for i in range(hidden_size):
      self.output_weights.append([])
      for j in range(output_size):
        self.output_weights[i].append(random.uniform(-.5, .5))
    print(self.input_weights)
    return self.input_weights, self.output_weights

  def compute_output(self, inputs):
    # input activations
    for i in range(self.input_size -1): # -1 is to avoid the bias
        self.ai[i] = inputs[i]
    # hidden activations
    for j in range(self.hidden_size):
        sum = 0.0
        for i in range(self.input_size):
            sum += self.ai[i] * self.wi[i][j]
        self.ah[j] = self.sigmoid(sum)
    # output activations
    for k in range(self.output_size):
        sum = 0.0
        for j in range(self.hidden_size):
            sum += self.ah[j] * self.wo[j][k]
        self.ao[k] = self.sigmoid(sum)
    return self.ao[:]

  def sigmoid(self, x):
    return 1 / (1 + np.exp(-x))

  def get_weights(self):
    return self.wi, self.wo


if __name__ == '__main__':
  app = NN()
  #app.construct_init_nn(5, 4, 2)
  app.set_NN_weights([[1,1],[2,2]],[[2,2],[2,2]])

  app.compute_output([2,2])



