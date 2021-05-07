import os
os.chdir('C:\\Users\\reetb\\Desktop\\epiDAMIK21\\Sims\\')

import covasim as cv

simB = cv.load('India100kBefore.sim')
sim1 = cv.load('India100kAfterPREEMPT.sim')
sim2 = cv.load('India100kAfterDegree.sim')
sim3 = cv.load('India100kAfterRandom.sim')


simB.label = 'No Vaccine'
sim1.label = 'PREEMPT Vaccines'
sim2.label = 'Degree Vaccines'
sim3.label = 'Random Vaccines'

msim = cv.MultiSim([simB, sim1, sim2, sim3]) 
msim.run()
msim.plot().savefig('plot12.png', dpi = 500)

