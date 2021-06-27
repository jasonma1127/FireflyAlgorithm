import numpy as np
import random as rand
import math
import time

class FireflyAlgorithm:

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
            self.functionArray[i] = self.func(self.populationArray[i,:], self.D)
                
    def update(self, i, j):
        scale = self.Ub - self.Lb
        r = 0
        for k in range(self.D):
            r += (self.populationArray[i][k] - self.populationArray[j][k])**2
        beta = self.beta0*math.exp(-self.gamma*r)
        for k in range(self.D):
            steps = (self.alpha*self.theta)*(rand.random() - 0.5)*scale
            self.tmpArray[k] = self.populationArray[i][k] + beta*(self.populationArray[j][k] - self.populationArray[i][k]) + steps
        if(self.func(self.tmpArray, self.D) < self.functionArray[i]):
            for k in range(self.D):
                self.populationArray[i][k] = self.tmpArray[k]
            self.functionArray[i] = self.func(self.tmpArray, self.D)
            
    def doRun(self):
        start = time.time()
        self.init_FA()
        for gen in range(self.iter_max):
            print("Generation ", gen+1)
            for i in range(self.n):
                for j in range(self.n):
                    if(self.functionArray[i] > self.functionArray[j] and i != j):
                        self.update(i,j)
            print(self.populationArray)
            print(self.functionArray)
        end = time.time()
        print("執行時間：%f 秒" % (end - start))
        return self.functionArray.min()
