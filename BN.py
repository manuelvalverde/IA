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
        if (len(self.parents) == 0):
            self.pfinal.append(1-self.prob[0])
            self.pfinal.append(self.prob[0])
        elif (len(self.parents) == 1):
            if (evid[self.parents[0]] == 0):
                self.pfinal.append(1-self.prob[0])
                self.pfinal.append(self.prob[0])
            else:
                self.pfinal.append(1-self.prob[1])
                self.pfinal.append(self.prob[1])
        elif (len(self.parents) == 2):
            if (evid[self.parents[0]] == 0 and evid[self.parents[1]] == 0):
                self.pfinal.append(1-self.prob[0][0])
                self.pfinal.append(self.prob[0][0])

            elif (evid[self.parents[0]] == 0 and evid[self.parents[1]] == 1):
                self.pfinal.append(1-self.prob[0][1])
                self.pfinal.append(self.prob[0][1])

            elif (evid[self.parents[0]] == 1 and evid[self.parents[1]] == 0):
                self.pfinal.append(1-self.prob[1][0])
                self.pfinal.append(self.prob[1][0])

            elif (evid[self.parents[0]] == 1 and evid[self.parents[1]] == 1):
                self.pfinal.append(1-self.prob[1][1])
                self.pfinal.append(self.prob[1][1])
        return self.pfinal

class BN():
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob
        self.list_evid = []
        self.mult = []
        self.all = []
        self.all_temp = []

    def computePostProb(self, evid):
        self.mult= []
        self.all = []
        self.list_evid = list(evid)
        soma_final = 0
        soma_final_aux = 0
        for i in range(len(self.list_evid)):
            if (self.list_evid[i] == 0):
                self.mult.append(self.prob[i].computeProb(evid)[0])
            elif (self.list_evid[i] == 1):
                self.mult.append(self.prob[i].computeProb(evid)[1])
        for j in range(len(self.mult)-1):
            self.mult[j+1] = self.mult[j] * self.mult[j+1]
        alpha = 1/self.mult[-1]
        for i1 in range(len(self.list_evid)):
            if (self.list_evid[i1] == -1):
                self.list_evid[i1] = 1
                self.all.append(self.list_evid)
                break
        for i2 in range(len(self.list_evid)):
            if (self.list_evid[i2] == []):
                self.all_temp = []
                for e in self.all:
                    copy = list(e)
                    copy[i2] = 0
                    self.all_temp.append(copy)
                    e[i2] = 1
                    self.all_temp.append(e)
                self.all = []
                for new in self.all_temp:
                    self.all.append(new)
        for s in self.all:
            soma_final_aux += self.computeJointProb(s)
        soma_final = alpha * soma_final_aux
        return soma_final


    def computeJointProb(self, evid):
        self.mult = []
        for i in range (len(self.prob)):
            if evid[i] == 0:
                self.mult.append(self.prob[i].computeProb(evid)[0])
            elif evid[i] == 1:
                self.mult.append(self.prob[i].computeProb(evid)[1])
        for j in range(len(self.mult)-1):
            self.mult[j+1] = self.mult[j] * self.mult[j+1]
        return self.mult[-1]
