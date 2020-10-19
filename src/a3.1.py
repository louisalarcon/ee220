#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 09:45:24 2020

@author: louis
"""

import matplotlib.pyplot as plt
from si_prefix import si_format
import numpy as np
import os

# import our custom ngspice module
import ngspice_link as ngl

# setup the simulation configuration
cfg1 = {
        'ngspice' : '/Applications/ngspice/bin/ngspice', 
        'cir_dir' : '/Users/louis/Documents/UPEEEI/Classes/EE 220/2020_1/Activities/',
        'cir_file' : 'a3.1.sp',
        }

# create the ngspice objects
sim1 = ngl.ngspice(cfg1)

# run ngspice with the configuration above
sim1.run_ngspice()

dfile = ['nmos_transfer_tt.dat', 'nmos_transfer_ff.dat', 'nmos_transfer_ss.dat']
ids = [[] for i in range(len(dfile))]

# read simulation output files
for i, f in enumerate(dfile):
    vgs, [ids[i]] = sim1.read_dc_analysis(f, [1])  
    
plt_cfg = {
        'grid_linestyle' : 'dotted',
        'title' : r'NMOS Transfer Characteristics W=100$\mu$m L=45nm',
        'xlabel' : r'$V_{GS}$ [mV]',
        'ylabel' : r'$I_{D}$ [mA]',
        'legend_loc' : 'lower right',
        'add_legend' : True,
        'legend_title' : r'$V_{DS}$=1V'
        }

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot([v/1e-3 for v in vgs], [i/1e-3 for i in ids[0]], '-', label='TT')
ax.plot([v/1e-3 for v in vgs], [i/1e-3 for i in ids[1]], '-', label='FF')
ax.plot([v/1e-3 for v in vgs], [i/1e-3 for i in ids[2]], '-', label='SS')

ngl.label_plot(plt_cfg, fig, ax)
plt.savefig('NMOS_transfer_corners.png', dpi=600)

plt_cfg = {
        'grid_linestyle' : 'dotted',
        'title' : r'NMOS Transfer Characteristics W=100$\mu$m L=45nm',
        'xlabel' : r'$V_{GS}$ [mV]',
        'ylabel' : r'$I_{D}$ [mA]',
        'legend_loc' : 'lower right',
        'add_legend' : True,
        'legend_title' : r'$V_{DS}$=1V'
        }

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogy([v/1e-3 for v in vgs], [i/1e-3 for i in ids[0]], '-', label='TT')
ax.semilogy([v/1e-3 for v in vgs], [i/1e-3 for i in ids[1]], '-', label='FF')
ax.semilogy([v/1e-3 for v in vgs], [i/1e-3 for i in ids[2]], '-', label='SS')

ngl.label_plot(plt_cfg, fig, ax)
plt.savefig('NMOS_log_transfer_corners.png', dpi=600)



dfile = ['nmos_output_tt.dat', 'nmos_output_ff.dat', 'nmos_output_ss.dat']
ids_raw = [[] for i in range(len(dfile))]

# read simulation output files
for i, f in enumerate(dfile):
    vds_raw, [ids_raw[i]] = sim1.read_dc_analysis(f, [1])  

# get the size of the data
# c - number of points in the inner DC sweep
# n - number of outer DC sweeps
c = 0
for i, v in enumerate(vds_raw):
    if i > 0 and v == vds_raw[0]:
        break
    c += 1
n = int(len(vds_raw)/c)

# reshape the result list
vds = [[] for i in range(len(dfile))]
ids = [[] for i in range(len(dfile))]

vds = np.reshape(vds_raw, (n, c))
for k in range(len(dfile)):
    ids[k] = np.reshape(ids_raw[k], (n, c))

plt_cfg = {
        'grid_linestyle' : 'dotted',
        'title' : r'NMOS Output Characteristics W=100$\mu$m L=45nm',
        'xlabel' : r'$V_{DS}$ [mV]',
        'ylabel' : r'$I_{D}$ [mA]',
        'legend_loc' : 'upper left',
        'add_legend' : True,
        'legend_title' : r'$V_{GS}$'
        }

l = ['0.2V', '0.4V', '0.6V', '0.8V', '1V']

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for k in range(n):
    plt.plot([v/1e-3 for v in vds[k]], [i/1e-3 for i in ids[0][k]], '-', label=l[k])
    
ngl.label_plot(plt_cfg, fig, ax)
plt.savefig('NMOS_output_tt.png', dpi=600)

plt_cfg = {
        'grid_linestyle' : 'dotted',
        'title' : r'NMOS Output Characteristics W=100$\mu$m L=45nm',
        'xlabel' : r'$V_{DS}$ [mV]',
        'ylabel' : r'$I_{D}$ [mA]',
        'legend_loc' : 'upper left',
        'add_legend' : True,
        'legend_title' : r'$V_{GS}$'
        }

l = ['0.2V', '0.4V', '0.6V', '0.8V', '1V']

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for k in range(n):
    plt.plot([v/1e-3 for v in vds[k]], [i/1e-3 for i in ids[0][k]], '-', label=l[k])
    
ax.set_prop_cycle(None)

for k in range(n):
    plt.plot([v/1e-3 for v in vds[k]], [i/1e-3 for i in ids[1][k]], ':')
    
ax.set_prop_cycle(None)

for k in range(n):
    plt.plot([v/1e-3 for v in vds[k]], [i/1e-3 for i in ids[2][k]], ':')

ngl.label_plot(plt_cfg, fig, ax)
plt.savefig('NMOS_output_corners.png', dpi=600)
        
