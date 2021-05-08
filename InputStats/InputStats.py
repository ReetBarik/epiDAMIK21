# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:30:23 2021

@author: reetb
"""

import os
os.chdir('C:\\Users\\reetb\\Desktop\\epiDAMIK21\\InputStats\\')

import networkx as nx
import numpy as np
import pandas as pd
import collections
import matplotlib.pyplot as plt

edgelist = 'India_100k.edgelist'
G = nx.read_weighted_edgelist(edgelist, nodetype = int, create_using = nx.DiGraph)

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
degree_sequence = [d/2 for d in degree_sequence]
meanDegree = np.average(degree_sequence)
stdDegree = np.std(degree_sequence)
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color="b")
frequency = 5
plt.xticks(deg[::frequency])
plt.title("Degree Histogram")
plt.ylabel("Count of Nodes")
plt.xlabel("Degree")
#ax.set_xticks([d + 0.4 for d in deg])
#ax.set_xticklabels(deg)
fig.text(0.65, 0.72, 'Mean = ' + "{:.2f}".format(meanDegree))
fig.text(0.65, 0.68, 'Std. Dev = ' + "{:.2f}".format(stdDegree))

plt.savefig('DegreeDistribution.PNG', dpi = 500)


#df = pd.read_csv(edgelist, sep = ' ', header = None)
#df1 = df[2]<0.05
#df1 = df[df1]
#
#df2 = df[2]>0.05
#df2 = df[df2]
#ax1 = df1[2].plot.hist(bins=10, alpha=0.5)
#ax2 = df2[2].plot.hist(bins=10, alpha=0.5)