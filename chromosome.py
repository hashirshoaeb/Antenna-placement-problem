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

    def update(self, chromosome):
        self.chrom = chromosome.chrom
        self.cal_fitness()

    def crossover(self, chromosome, position): # postion range 1-4, no error range 0-5
        for i in range(0,position):
                self.chrom[i], chromosome.chrom[i] = chromosome.chrom[i], self.chrom[i]
        self.cal_fitness()
        chromosome.cal_fitness()

    def mutate(self):
        num1 = r.choice([1,2,3,4,5,6])
        num2 = r.choice([1,2,3,4,5,6])
        position = r.choice([0,1,2,3,4])
        self.chrom[position] = [num1, num2]
        self.cal_fitness()