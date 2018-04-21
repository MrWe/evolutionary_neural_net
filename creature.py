import numpy as np

class Creature(object):
  """docstring for Creature."""
  def __init__(self, health, speed, coords):
    self.health = health
    self.speed = speed
    self.coords = np.array(coords)
    self.input = []


  def move(self, direction):
    #print(np.sign(np.array(direction)))
    if(not(self.coords[0] < 5 or self.coords[0] > 495 or self.coords[1] < 5 or self.coords[1] > 495)):
      if(direction[0] >= 0.5):
        direction[0] = 1
      else:
        direction[0] = -1
      if(direction[1] >= 0.5):
        direction[1] = 1
      else:
        direction[1] = -1
      print(direction)
      self.coords = np.add(self.coords, np.array(direction))
    else:
      self.score -= 2


  def is_near(self, other):
    pass