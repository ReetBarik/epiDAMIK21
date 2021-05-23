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
msim.plot(to_plot=['cum_infections'], do_save=True, fig_path='Fig4CI.png', mpl_args={'dpi':500, 'font_size':15}) #, plot_args={'linestyle' : ['solid', 'dashed', 'dash_dot', 'dotted', '.-.']}, )
msim.plot(to_plot=['new_infections'], do_save=True, fig_path='Fig4NI.png', mpl_args={'dpi':500, 'font_size':15}) #, plot_args={'linestyle' : ['solid', 'dashed', 'dash_dot', 'dotted', '.-.']}, )
msim.plot(to_plot=['cum_deaths'], do_save=True, fig_path='Fig4CD.png', mpl_args={'dpi':500, 'font_size':15}) #, plot_args={'linestyle' : ['solid', 'dashed', 'dash_dot', 'dotted', '.-.']}, )

# msim.run()
# msim.plot_result('cum_infections').savefig('Fig4CI.png', dpi = 500)
# msim.plot_result('new_infections').savefig('Fig4NI.png', dpi = 500)
# msim.plot_result('cum_deaths').savefig('Fig4CD.png', dpi = 500)
