import numpy as np

class Creature(object):
  """docstring for Creature."""
  def __init__(self, health, speed, coords):
    self.health = health
    self.speed = speed
    self.coords = np.array(coords)
    self.input = []

  def move(self, dir_x, dir_y):
    if(not(self.coords[0] < 5 or self.coords[0] > 495 or self.coords[1] < 5 or self.coords[1] > 495)):
      np.add(self.coords, np.array(dir_x, dir_y))
    else:
      self.score -= 2


  def is_near(self, other):
    pass