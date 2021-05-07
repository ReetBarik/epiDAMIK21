# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:01:03 2021

@author: reetb
"""

import os
os.chdir('C:\\Users\\reetb\\Desktop\\epiDAMIK21\\')

import covasim as cv
import json 
import numpy as np
import random
from random import randrange
import networkx as nx


# Seed selection Strategy: 0 for PREEMPT, 1 for Random, 2 for Degree
choice = 2

# Seeds based on Degree
def generateDegreeSeeds():

	edgelist = 'India_100k_PREEMPT.edgelist'
	G = nx.read_weighted_edgelist(edgelist, nodetype = int, create_using = nx.DiGraph)

	deg = sorted(G.degree, key=lambda x: x[1], reverse=True)
	seeds = []
	for s,d in deg[0:12500]:
		seeds.append(s)

	np.savetxt('India100kSeeds_Degree.txt', seeds, fmt='%d', delimiter=' ')

	return seeds


# PREEMPT prescribed seeds
def generateSeeds():

	filename = 'India_100k.json'		 

	with open(filename) as json_file: 
		data = json.load(json_file)

	seeds = list(data[0]['Seeds'])

	return seeds

# Random seeds
def generateRandomSeeds():

	r_seeds = 0
	random.seed(a = r_seeds)

	previousSeeds = set()
	seeds = []

	while (len(seeds) < 12500):
		seed = randrange(100000)
		if (seed not in previousSeeds):
			seeds.append(seed)
			previousSeeds.add(seed)

	np.savetxt('India100kSeeds_Random.txt', seeds, fmt='%d', delimiter=' ')
	return seeds


# Returns a dict of node indices as key and their probability of getting vaccinated as values
def vaccinateSeeds(sim, seeds):
	inds = sim.people.uid
	vals = np.zeros(len(sim.people))

	# set of seeds chosen by PREEMPT to have a 100% probability of getting vaccinated
	for seed in seeds:
		vals[seed] = 1.0

	output = dict(inds=inds, vals=vals)
	return output


sim2 = cv.load('India100kBefore.sim')

if (choice == 0):
	seeds = generateSeeds()
if (choice == 1):
	seeds = generateRandomSeeds()
if (choice == 2):
	seeds = generateDegreeSeeds()


# Define the vaccine and add it to the sim
vaccine =  cv.simple_vaccine(days=31, rel_sus=0.0, rel_symp=0.02, subtarget=vaccinateSeeds(sim2, seeds))
vaccine.vaccinations = vaccine.subtarget['vals'].astype(int)
vaccine.initialize(sim2)
sim2.pars['interventions'].append(vaccine)

# setting 'rel_trans' od vaccinated seeds ensure edge probability on outgoing edges are set to zero
for seed in seeds:
	sim2.people.rel_trans[seed] = 0.0
	
# Let it run for a week
sim2.run(until='2020-05-30')
	
# Save the sim
sim2.save('India100kAfter.sim')

