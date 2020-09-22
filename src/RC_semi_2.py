#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 19:21:42 2020

@author: louis
"""

import matplotlib.pyplot as plt
from si_prefix import si_format
import numpy as np
import os

# import our custom ngspice module
import ngspice_link as ngl

# setup the simulation configuration
cfg = {
        'ngspice' : '/Applications/ngspice/bin/ngspice', 
        'cir_dir' : '/Users/louis/Documents/UPEEEI/Classes/EE 220/2020_1/Activities/',
        'cir_file' : 'RC_semi_a2.1.sp',
        }

# create the ngspice object
sim1 = ngl.ngspice(cfg)

# delete old output file if it exists.
dfile = 'mc_RC.dat'
if os.path.isfile(dfile):
    os.remove(dfile)

# run ngspice with the configuration above
sim1.run_ngspice()

runs, [R1, C1, fc] = sim1.read_dc_analysis(dfile, [1,2,3])    

R1_mean = np.mean(R1)
R1_var = np.var(R1)

C1_mean = np.mean(C1)
C1_var = np.var(C1)

fc_mean = np.mean(fc)
fc_var = np.var(fc)

plt_cfg = {
        'grid_linestyle' : 'dotted',
        'title' : r'$f_c$: $\mu=${:.2f}, $\sigma=${:.2f} (N={})'.format( \
            fc_mean, np.sqrt(fc_var), len(runs)),
        'xlabel' : r'Frequency [Hz]',
        'ylabel' : r'Count',
        'legend_loc' : 'lower left',
        'add_legend' : False,
        'legend_title' : None
        }

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist(x=fc, bins=20, rwidth=0.85)
ngl.label_plot(plt_cfg, fig, ax)
plt.savefig('fc_hist.png', dpi=600)


plt_cfg = {
        'grid_linestyle' : 'dotted',
        'title' : r'$R_1$: $\mu=${:.2f}, $\sigma=${:.2f} (N={})'.format( \
            R1_mean, np.sqrt(R1_var), len(runs)),
        'xlabel' : r'$R_1$ [$\Omega$]',
        'ylabel' : r'Count',
        'legend_loc' : 'lower left',
        'add_legend' : False,
        'legend_title' : None
        }

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist(x=R1, bins=20, rwidth=0.85)
ngl.label_plot(plt_cfg, fig, ax)
plt.savefig('R_hist.png', dpi=600)

plt_cfg = {
        'grid_linestyle' : 'dotted',
        'title' : r'$C_1$: $\mu=${:.2e}, $\sigma=${:.2e} (N={})'.format( \
            C1_mean, np.sqrt(C1_var), len(runs)),
        'xlabel' : r'$C_1$ [F]',
        'ylabel' : r'Count',
        'legend_loc' : 'lower left',
        'add_legend' : False,
        'legend_title' : None
        }

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist(x=C1, bins=20, rwidth=0.85)
ngl.label_plot(plt_cfg, fig, ax)
plt.savefig('C_hist.png', dpi=600)

plt_cfg = {
        'grid_linestyle' : 'dotted',
        'title' : r'RC Scatter Plot (N={})'.format(len(runs)),
        'xlabel' : r'$R_1$ [$\Omega$]',
        'ylabel' : r'$C_1$ [F]',
        'legend_loc' : 'lower left',
        'add_legend' : False,
        'legend_title' : None
        }

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(R1, C1, 'o')
ngl.label_plot(plt_cfg, fig, ax)
plt.savefig('RC_scatter.png', dpi=600)

