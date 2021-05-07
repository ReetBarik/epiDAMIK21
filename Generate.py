# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:00:52 2021

@author: reetb
"""

import os
os.chdir('C:\\Users\\reetb\\Desktop\\epiDAMIK21\\')

import covasim as cv
import networkx as nx
import numpy as np

pars = dict(
	pop_size = 100000,                                                      
	pop_type = 'hybrid',
	location = 'India',
	pop_infected = 100,
	start_day = '2020-01-01',
	end_day = '2020-05-30'
)

sim = cv.Sim(pars)
sim.run(until='2020-01-30')

sim.save('India100kBefore.sim')


G = nx.DiGraph()
G.add_nodes_from(sim.people.uid)

layers = ['h', 's', 'c', 'w']

for layer in layers:
	contacts = sim.people.contacts[layer]

	for i in range(len(contacts)):
		p1 = contacts['p1'][i]						   # Source
		p2 = contacts['p2'][i]						   # Destination

	    # For the weight on p1 -> p2
		probabilityP1_P2 = sim.pars['beta_layer'][layer] * sim.pars['beta'] * sim.people.rel_trans[p1] * sim.people.rel_sus[p2]
	    # For the weight on p2 -> p1
		probabilityP2_P1 = sim.pars['beta_layer'][layer] * sim.pars['beta'] * sim.people.rel_trans[p2] * sim.people.rel_sus[p1]

	      # Capping the edge weight at 1
		if (probabilityP1_P2 > 1):
			probabilityP1_P2 = 1

		if (probabilityP2_P1 > 1):
			probabilityP2_P1 = 1

	    # Eliminate duplicate edge by retaining max weight
		if (G.has_edge(p1,p2)):
			G.add_edge(p1, p2, weight = max(G[p1][p2]['weight'],'{:.6f}'.format(probabilityP1_P2)))
				
		else:
			G.add_edge(p1, p2, weight = '{:.6f}'.format(probabilityP1_P2))
				
	    # Eliminate duplicate edge by retaining max weight
		if (G.has_edge(p2,p1)):
			G.add_edge(p2, p1, weight = max(G[p2][p1]['weight'],'{:.6f}'.format(probabilityP2_P1)))
				
		else:
			G.add_edge(p2, p1, weight = '{:.6f}'.format(probabilityP2_P1))

# Edgelist with all edges to investigate shift in PDF as a result of vaccination
nx.write_weighted_edgelist(G, 'India_100k.edgelist')

# Set of nodes with 'rel_sus' == 0 is the union of already vaccinated nodes and recovered nodes.  
removeNodes = np.where(sim.people['rel_sus'] == 0)[0]

for node in removeNodes:							   # No need to vaccinate, hence PREEMPT shouldn't see them							  
	G.remove_node(node)

# Generate the input edgelist for PREEMPT
nx.write_weighted_edgelist(G, 'India_100k_PREEMPT.edgelist')