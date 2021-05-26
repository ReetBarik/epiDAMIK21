import covasim as cv
from cycler import cycler
import matplotlib.pyplot as plt
plt.rc('axes', prop_cycle= cycler(linestyle=['-', '--', ':', '-.', (0, (5, 1, 1, 1, 1, 1))]))

simB = cv.load('Baseline.sim')
sim1 = cv.load('Degree_1000_20.sim')
sim2 = cv.load('Degree_hybrid.sim')
sim3 = cv.load('PREEMPT_1000_20.sim')
sim4 = cv.load('PREEMPT_hybrid.sim')


simB.label = 'No Vaccine'
sim1.label = 'Degree_uniform'
sim2.label = 'Degree_non-uniform'
sim3.label = 'PREEMPT_uniform'
sim4.label = 'PREEMPT_non-uniform'

msim = cv.MultiSim([simB, sim1, sim2, sim3, sim4]) 
msim.run()
msim.plot(to_plot=['cum_infections'], plot_args={'lw':5}, mpl_args={'font_size':17}).savefig('Fig5CI.png', dpi = 1000) 
msim.plot(to_plot=['new_infections'], plot_args={'lw':5}, mpl_args={'font_size':17}).savefig('Fig5NI.png', dpi = 1000)
msim.plot(to_plot=['cum_deaths'], plot_args={'lw':5}, mpl_args={'font_size':17}).savefig('Fig5CD.png', dpi = 1000)
