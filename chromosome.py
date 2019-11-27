import numpy as np
import random as r

class chromosome:
    # this will generate a random chromosome
    def __init__(self):
        list = [1,2,3,4,5,6]
        self.chrom = []
        for i in range(0,5):
                self.chrom = self.chrom + [[r.choice(list),r.choice(list)]]