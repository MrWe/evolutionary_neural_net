from creature import Creature
from nn import NN
import numpy as np

class Harvester(Creature):
  """docstring for Harvester."""
  def __init__(self, health, speed, coords, dna):
    Creature.__init__(self, health, speed, coords)
    self.weights = np.random.uniform(-1,1, 10)
    self.output = np.random.uniform(-1,1, 2)
    self.actions = []
    self.lifespan = 0
    self.score = 0
    self.dna = dna
    self.action_nn = NN()
    self.move_nn = NN()

  def set_score(self):
    self.score = self.lifespan

  def update(self):
    self.lifespan += 1

  def harvest(self):
    pass

  def move_to_supplies(self, supplies_list, lr):
    sh = float("inf")
    nearest_coords = []
    for i in range(len(supplies_list)):
      d = np.linalg.norm(self.coords - supplies_list[i].coords)
      if d < sh:
        sh = d
        nearest_coords = supplies_list[i].coords
    direction = np.subtract(self.coords, nearest_coords)
    direction = np.multiply(direction, lr)
    self.coords = np.subtract(self.coords, direction)

  def sight(self, hunters_list, supplies_list, storages_list, max_distance):
    self.input = []
    for i in range(len(hunters_list)):
      self.input.append(1-(np.linalg.norm(self.coords - hunters_list[i].coords)/max_distance))
    for i in range(len(supplies_list)):
      self.input.append(1-(np.linalg.norm(self.coords - supplies_list[i].coords)/max_distance))
    for i in range(len(storages_list)):
      self.input.append(1-(np.linalg.norm(self.coords - storages_list[i].coords)/max_distance))

  def get_action():
    pass



