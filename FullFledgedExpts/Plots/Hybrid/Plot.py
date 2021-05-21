import covasim as cv

simB = cv.load('Baseline.sim')
sim1 = cv.load('Degree_1000_20.sim')
sim2 = cv.load('Degree_hybrid.sim')
sim3 = cv.load('PREEMPT_1000_20.sim')
sim4 = cv.load('PREEMPT_hybrid.sim')


simB.label = 'No Vaccine'
sim1.label = 'Degree_1000_20'
sim2.label = 'Degree_hybrid'
sim3.label = 'PREEMPT_1000_20'
sim4.label = 'PREEMPT_hybrid'

msim = cv.MultiSim([simB, sim1, sim2, sim3, sim4]) 
msim.run()
msim.plot().savefig('plot12.png', dpi = 500)