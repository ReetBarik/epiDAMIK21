import covasim as cv

simB = cv.load('Baseline.sim')
sim1 = cv.load('Degree_20000_1.sim')
sim2 = cv.load('Degree_1000_20.sim')
sim3 = cv.load('PREEMPT_20000_1.sim')
sim4 = cv.load('PREEMPT_1000_20.sim')


simB.label = 'No Vaccine'
sim1.label = 'Degree_20000_1'
sim2.label = 'Degree_1000_20'
sim3.label = 'PREEMPT_20000_1'
sim4.label = 'PREEMPT_1000_20'

msim = cv.MultiSim([simB, sim1, sim2, sim3, sim4]) 
msim.run()
msim.plot().savefig('plot12.png', dpi = 500)