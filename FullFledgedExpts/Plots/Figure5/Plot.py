import covasim as cv
from cycler import cycler
import matplotlib.pyplot as plt
plt.rc('axes', prop_cycle= cycler(linestyle=['-', '--', ':', '-.', (0, (5, 1, 1, 1, 1, 1))]))

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
msim.plot(to_plot=['cum_infections'], plot_args={'lw':5}, mpl_args={'font_size':17}).savefig('Fig4CI.png', dpi = 1000) 
msim.plot(to_plot=['new_infections'], plot_args={'lw':5}, mpl_args={'font_size':17}).savefig('Fig4NI.png', dpi = 1000)
msim.plot(to_plot=['cum_deaths'], plot_args={'lw':5}, mpl_args={'font_size':17}).savefig('Fig4CD.png', dpi = 1000)
