# -*- coding: utf-8 -*-
"""
Created on Thu May 13 17:51:07 2021

@author: reetb
"""

import os
os.chdir('C:\\Users\\reetb\\Desktop\\epiDAMIK21\\HistogramExpts\\')


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#fig, ax = plt.subplots()

index = ['2.5', '5.0', '10.0', '12.5', '15.0', '20.0']

ci_no = [84997, 84997, 84997, 84997, 84997, 84997]

ci_random = [82030, 79296, 73753, 70974, 68035, 61854]

ci_degree = [81499, 78226, 71586, 68294, 64690, 57229]

ci_PREEMPT = [77472, 69370, 54443, 47702, 41671, 33004]

ci_no = [x/1000 for x in ci_no]

ci_random = [x/1000 for x in ci_random]

ci_degree = [x/1000 for x in ci_degree]

ci_PREEMPT = [x/1000 for x in ci_PREEMPT]

df = pd.DataFrame({'Random': ci_random,'Degree': ci_degree, 'PREEMPT': ci_PREEMPT}, index=index)

ax = df.plot.bar(rot=0) 
bars = ax.get_children()[0:18]
for i in range(0,6):
    bars[i].set_hatch('\\')

#for i in range(6,12):
#    bars[i].set_hatch('x')
    
for i in range(12,18):
    bars[i].set_hatch('.')

ax.plot(ci_no, color = 'red', marker = 'o', linestyle='dashed', linewidth=0.5, markersize=2, label = 'No vaccine', alpha = 0.75)
ax.set_ylim(20,95)
plt.legend(loc="upper right", ncol=len(df.columns) + 1, prop={'size': 9})
plt.ylabel("Cumulative #infections (as a % of population)")
plt.xlabel("% of population vaccinated")
plt.title("Effect of seed selection strategies on disease spread")
plt.savefig('CI_Hist.png', dpi = 500)