import numpy as np
import random
import math

class NN(object):
  """docstring for NN."""
  def __init__(self):
    self.input_weights = []
    self.output_weights = []

  def set_NN_weights(self, input_weights, output_weights):
    self.input_weights = input_weights
    self.output_weights = output_weights

  def construct_init_nn(self, input_size, hidden_size, output_size):
    for i in range(input_size):
      self.input_weights.append([])
      for j in range(hidden_size):
        self.input_weights[i].append(random.uniform(-.5, .5))
    for i in range(hidden_size):
      self.output_weights.append([])
      for j in range(output_size):
        self.output_weights[i].append(random.uniform(-.5, .5))
    return self.input_weights, self.output_weights

  def compute_output(self, input_data):
    hidden_neurons = []
    for n in range(len(self.input_weights[0])):
      for i in range(len(input_data)):
        activation = 0
        for j in range(len(self.input_weights)):
          activation += input_data[i] * self.input_weights[j][n]
      activation_function = 1/(math.exp(-activation))
      hidden_neurons.append(activation_function)

    output_neurons = []
    for n in range(len(self.output_weights[0])):
      for i in range(len(hidden_neurons)):
        activation = 0
        for j in range(len(self.output_weights)):
          activation += hidden_neurons[i] * self.output_weights[j][n]
      output_neurons.append(activation)

    return output_neurons


if __name__ == '__main__':
  app = NN()
  #app.construct_init_nn(5, 4, 2)
  app.set_NN_weights([[1,1],[2,2]],[[2,2],[2,2]])

  app.compute_output([2,2])



