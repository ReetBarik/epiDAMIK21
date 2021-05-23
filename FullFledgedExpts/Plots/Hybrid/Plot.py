import covasim as cv

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
msim.plot(to_plot=['cum_infections'], do_save=True, fig_path='Fig5CI.png', mpl_args={'dpi':500, 'font_size':15}) #, plot_args={'linestyle' : ['solid', 'dashed', 'dash_dot', 'dotted', '.-.']}, )
msim.plot(to_plot=['new_infections'], do_save=True, fig_path='Fig5NI.png', mpl_args={'dpi':500, 'font_size':15}) #, plot_args={'linestyle' : ['solid', 'dashed', 'dash_dot', 'dotted', '.-.']}, )
msim.plot(to_plot=['cum_deaths'], do_save=True, fig_path='Fig5CD.png', mpl_args={'dpi':500, 'font_size':15}) #, plot_args={'linestyle' : ['solid', 'dashed', 'dash_dot', 'dotted', '.-.']}, )
