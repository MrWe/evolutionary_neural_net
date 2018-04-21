from harvester import Harvester
from hunter import Hunter
from storage import Storage
from supply import Supply
from dna import DNA
import random
import numpy as np

harvester_actions = {0: [2, 2]}

num_harvesters = 1
num_hunters = 10
num_storages = 10
num_supplies = 10

def get_fitness(population):
  sorted_population = sorted(population, key=lambda x: x.score, reverse=True)
  mating_pool = []

  for i in range(len(sorted_population)):
    for j in range(int(100*(1/(i+1)))):
      mating_pool.append(sorted_population[i])
  return sorted_population


def generate_harvesters_population(sorted_population):
  new_population = []
  parents = []

  for i in range(num_harvesters):
    dna = crossover(sorted_population[random.randint(0, len(sorted_population)-1)], sorted_population[random.randint(0, len(sorted_population)-1)])
    new_population.append(Harvester(random.randint(0,10),random.randint(0,10),[random.randint(0,500),random.randint(0,500)], dna))
  return new_population

def crossover(p1, p2):
  dna = []
  for i in range(len(p1.dna)):
    for j in range(len(p1.dna[i])):
      if(len(p1.dna[i][j]) == 1):
        dna.append(get_random_parent_gene(p1.dna[i][j], p2.dna[i][j]))
      else:
        gene = []
        for k in range(len(p1.dna[i][j])):
          gene.append(get_random_parent_gene(p1.dna[i][j][k], p2.dna[i][j][k]))
        dna.append(gene)

  return [dna]


def get_random_parent_gene(g1, g2):
  return g1 if random.uniform(0,1) > 0.5 else g2



def init():
  harvesters = []
  hunters = []
  storages = []
  supplies = []


  for i in range(num_harvesters):
    harvesters.append(Harvester(random.randint(0,10),random.randint(0,10),[random.randint(0,500),random.randint(0,500)], None))
  #print(dna)

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