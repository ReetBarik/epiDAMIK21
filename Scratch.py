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

import matplotlib.pyplot as plt

x = [2500, 5000, 10000, 12500, 15000]

ci_random = [82031, 79297, 73753, 70972, 68036]

ci_degree = [81500, 78227, 71584, 68294, 64688]

ci_PREEMPT = [76992, 68623, 54303, 48151, 41352]

ci_noVaccine = [84997, 84997, 84997, 84997, 84997]

fig, ax = plt.subplots()
#ax.set_xticklabels(['2.5k', '5k', '10k', '12.5k', '15k'])
ax.plot(x, ci_noVaccine, marker='o' ,label='No Vaccines')
ax.plot(x, ci_random, marker='o' ,label='Random Vaccines')
ax.plot(x, ci_degree, marker='o' ,label='Degree Vaccines')
ax.plot(x, ci_PREEMPT, marker='o' ,label='PREEMPT Vaccines')

ax.set_xlabel('% of Population Vaccinated') 
ax.set_ylabel('Cumulative infections after 5 months') 
ax.legend()
plt.savefig('Result.PNG', dpi = 500)
