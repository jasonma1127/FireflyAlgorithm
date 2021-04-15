import numpy as np
import random as rand
import math

class FireflyAlgorithm():

    def __init__(self, D, Lb, Ub, n, alpha, beta0, gamma, theta, iter_max, func):
        self.D = D
        self.Lb = Lb
        self.Ub = Ub
        self.n = n
        self.alpha = alpha
        self.beta0 = beta0
        self.gamma = gamma
        self.theta = theta
        self.iter_max = iter_max
        self.func = func
        self.populationArray = np.zeros((n, D))
        self.functionArray = np.zeros(n)
        self.tmpArray = np.zeros(D)
    
    def init_FA(self):
        for i in range(self.n):
            for j in range(self.D):
                self.populationArray[i][j] = rand.uniform(self.Lb, self.Ub)
                self.functionArray[i] = func(self.populationArray[i][0], self.populationArray[i][1])
                
    def update(self, i, j):
        scale = self.Ub - self.Lb
        r = (self.populationArray[i][0] - self.populationArray[j][0])**2 + (self.populationArray[i][1] - self.populationArray[j][1])**2
        beta = self.beta0*math.exp(-self.gamma*r)
        for k in range(self.D):
            steps = (self.alpha*self.theta)*(rand.random() - 0.5)*scale
            self.tmpArray[k] = self.populationArray[i][k] + beta*(self.populationArray[j][k] - self.populationArray[i][k]) + steps
        if(func(self.tmpArray[0], self.tmpArray[1]) < self.functionArray[i]):
            for k in range(self.D):
                self.populationArray[i][k] = self.tmpArray[k]
            self.functionArray[i] = func(self.tmpArray[0], self.tmpArray[1])
            
    def doRun(self):
        self.init_FA()
        for gen in range(self.iter_max):
            print("Generation ", gen+1)
            for i in range(self.n):
                for j in range(self.n):
                    if(self.functionArray[i] > self.functionArray[j] and i != j):
                        self.update(i,j)
            print(self.functionArray)
        return self.functionArray.min()
