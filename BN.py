# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""



class Node():
    def __init__(self, prob, parents = []):
        self.prob = prob
        self.parents = parents
        self.pfinal = []
    
    def computeProb(self, evid):
        if (len(parents) == 0):
            print(prob[0])
        elif (len(parents) == 1):
            if (evid[self.parents[0]] == 0):
                self.pfinal.append[(1-prob[0]]
                self.pfinal.append[prob[0]]
            else
                self.pfinal.append[(1-prob[1]]
                self.pfinal.append([prob[1]])
        else if (len(parents) == 2):
            if (evid[self.parents[0]] == 0 and evid[self.parents[1]] == 0]):
                self.pfinal.append[(1-prob[0][0]]
                self.pfinal.append([prob[0][0]])

            elif (evid[self.parents[0]] == 0 and evid[self.parents[1]] == 1]):
                self.pfinal.append[(1-prob[0][1]]
                self.pfinal.append([prob[0][1]])

            elif (evid[self.parents[0]] == 1 and evid[self.parents[1]] == 0]):
                self.pfinal.append[(1-prob[1][0]]
                self.pfinal.append([prob[1][0]])

            elif (evid[self.parents[0]] == 1 and evid[self.parents[1]] == 1]):
                self.pfinal.append[(1-prob[1][1]]
                self.pfinal.append([prob[1][1]])
        return self.pfinal
    
class BN():
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob
        self.mult = []
        self.all = []
        self.all_temp = []

    def computePostProb(self, evid):
        self.mult= []
        self.all = []
        soma_final = 0
        soma_final_aux = 0
        for i in range(len(evid)):
            if (evid[i] == 0):
                self.mult.append(prob[i].computeProb(evid)[0])
            elif (evid[i] == 1)
                self.mult.append(prob[i].computeProb(evid)[1])
        for j in range(len(self.mult)-1):
            self.mult[j+1] = self.mult[j] * self.mult[j+1]
        alpha = 1/self.mult[-1]
        for i1 in range(len(evid)):
            if (evid[i1] == -1):
                evid[i1] = 1
                self.all.append(evid)
        for i2 in range(len(evid)):
            if (evid[i2] == []):
                for e in self.all:
                    e[i2] = 0
                    self.all_temp.append(evid)
                    e[i2] = 1
                    self.all_temp.append(evid)
                self.all = []
                for new in self.all_temp:
                    self.all.append(new)
        for s in self.all:
            soma_final_aux + = self.computeJointProb(s)
        soma_final = alpha * soma_final_aux
        return 0
        
        
    def computeJointProb(self, evid):
        self.mult = []
        for i in range (len(prob)):
            if evid[i] == 0:
                self.mult.append(prob[i].computeProb(evid)[0])
            elif evid[i] == 1:
                self.mult.append(prob[i].computeProb(evid)[1])
        for j in range(len(self.mult)-1):
            self.mult[j+1] = self.mult[j] * self.mult[j+1]
        return self.mult[-1]