import numpy as np
import random as r

class chromosome:
    # this will generate a random chromosome
    def __init__(self):
        list = [1,2,3,4,5,6]
        self.chrom = []
        for i in range(0,5):
                self.chrom = self.chrom + [[r.choice(list),r.choice(list)]]
        self.cal_fitness()
        print(self.chrom, " with fitness ", self.fitnessValue)

    def cal_fitness(self):
        area = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0], ])
        for i, j in self.chrom:
            area[j - 1][i] = 1
            area[j][i - 1] = area[j][i] = area[j][i + 1] = 1
            area[j + 1][i] = 1
        self.area = area[1:7, 1:7]
        self.fitnessValue = self.area.sum()
        # print(self.area)
        # print(self.fitnessValue)
        return self.fitnessValue