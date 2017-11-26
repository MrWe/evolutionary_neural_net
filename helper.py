from harvester import Harvester
from hunter import Hunter
from storage import Storage
from supply import Supply
from dna import DNA
import random
import numpy as np

harvester_actions = {0: 2}

def get_fitness(population):
  sorted_population = sorted(population, key=lambda x: x.score, reverse=True)
  return sorted_population


def generate_harvesters_population(sorted_population):
  new_population = []

  while(len(new_population) < len(sorted_population)):
    parents = []
    for i in range(len(sorted_population)):
      if(1/i > 0.8):
        parents.append(sorted_population[i].dna)
      if(len(parents) == 2):
        new_population.append(crossover(parents))
        break




def crossover(parents):
  pass



def init():
  harvesters = []
  hunters = []
  storages = []
  supplies = []

  num_harvesters = 10
  num_hunters = 10
  num_storages = 10
  num_supplies = 10

  for i in range(num_harvesters):
    dna = [[]]
    for k in range(10):
      dna[0].append(random.uniform(-.5, .5))
    for j in range(len(harvester_actions)):
      dna.append([])
      for h in range(harvester_actions[j]):
        dna[j+1].append(random.uniform(-.5,.5))
    harvesters.append(Harvester(random.randint(0,10),random.randint(0,10),[random.randint(0,500),random.randint(0,500)], dna))

  for i in range(num_hunters):
    hunters.append(Hunter(random.randint(0,10),random.randint(0,10),[random.randint(0,500),random.randint(0,500)]))

  for i in range(num_storages):
    storages.append(Storage([random.randint(0,500),random.randint(0,500)]))

  for i in range(num_supplies):
    supplies.append(Supply([random.randint(0,500),random.randint(0,500)]))

  return np.array(harvesters), np.array(hunters), np.array(storages), np.array(supplies)



def run():
  harvesters = []
  harvesters.append(Harvester(1,2,[10,20]))
  return harvesters