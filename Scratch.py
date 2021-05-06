# -*- coding: utf-8 -*-
"""
Created on Wed May  5 14:24:13 2021

@author: reetb
"""

import os
os.chdir('C:\\Users\\reetb\\Desktop\\epiDAMIK21\\')

import covasim as cv
import numpy as np

pars = dict(
    pop_size = 100000,                       # Number of nodes
    pop_type = 'hybrid',							   # Hybrid population: household, school, work, community layer
    location = 'India',								   # Location and demographic based on India
    pop_infected = 1000,
    start_day = '2020-01-01',					   # Simulation start
    end_day = '2020-05-30'							   # Simulation end
)

sim = cv.Sim(pars)
sim.initialize()
#sim.run(until='2020-01-02')							   
np.count_nonzero(sim.people.exposed)


sim.run()
sim.plot()
sim.save('India100k.sim')		   # Save the sim

np.count_nonzero(sim.people.infectious)