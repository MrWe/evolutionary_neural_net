class DNA(object):
  """docstring for DNA."""
  def __init__(self, actions, parent_genes):
    self.dna = []
    if(parent_genes):
      self.create_random_dna(actions)



