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
    
# calculate the transconductance via numerical differentiation

def dydx(y, x):
    dy = np.diff(y)
    dx = np.diff(x)
    return dy/dx

gm = [dydx(i, vgs) for i in ids]
    
plt_cfg = {
        'grid_linestyle' : 'dotted',
        'title' : r'NMOS Transconductance W=1$\mu$m L=45nm',
        'xlabel' : r'$V_{GS}$ [mV]',
        'ylabel' : r'$g_m$ [mS]',
        'legend_loc' : 'lower right',
        'add_legend' : True,
        'legend_title' : r'$V_{DS}$=1V'
        }

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot([v/1e-3 for v in vgs[1:]], [g/1e-3 for g in gm[0]], '-', label='TT')
ax.plot([v/1e-3 for v in vgs[1:]], [g/1e-3 for g in gm[1]], '-', label='FF')
ax.plot([v/1e-3 for v in vgs[1:]], [g/1e-3 for g in gm[2]], '-', label='SS')

ngl.label_plot(plt_cfg, fig, ax)
plt.savefig('NMOS_gm_corners.png', dpi=600)


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
# vds = [[] for i in range(len(dfile))]
ids = [[] for i in range(len(dfile))]
ro = [[] for i in range(len(dfile))]

vds = np.reshape(vds_raw, (n, c))
for k in range(len(dfile)):
    ids[k] = np.reshape(ids_raw[k], (n, c))
    ro[k] = [1/dydx(i, vds[0]) for i in ids[k]]

plt_cfg = {
        'grid_linestyle' : 'dotted',
        'title' : r'NMOS Output Impedance W=1$\mu$m L=45nm',
        'xlabel' : r'$V_{DS}$ [mV]',
        'ylabel' : r'$r_o$ [k$\Omega$]',
        'legend_loc' : 'upper right',
        'add_legend' : True,
        'legend_title' : r'$V_{GS}$'
        }

l = ['0.2V', '0.4V', '0.6V', '0.8V', '1V']

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for k in range(2):
    plt.semilogy([v/1e-3 for v in vds[k][1:]], [r/1e3 for r in ro[0][k]], '-', label=l[k])
    
ax.set_prop_cycle(None)

for k in range(2):
    plt.semilogy([v/1e-3 for v in vds[k][1:]], [r/1e3 for r in ro[1][k]], ':')  

ax.set_prop_cycle(None)

for k in range(2):
    plt.semilogy([v/1e-3 for v in vds[k][1:]], [r/1e3 for r in ro[2][k]], ':')                                                                                       
                                                                                       
ngl.label_plot(plt_cfg, fig, ax)
plt.savefig('NMOS_ro_corners.png', dpi=600)

plt_cfg = {
        'grid_linestyle' : 'dotted',
        'title' : r'NMOS Output Impedance W=1$\mu$m L=45nm',
        'xlabel' : r'$V_{DS}$ [mV]',
        'ylabel' : r'$r_o$ [k$\Omega$]',
        'legend_loc' : 'lower right',
        'add_legend' : True,
        'legend_title' : r'$V_{GS}$'
        }

l = ['0.2V', '0.4V', '0.6V', '0.8V', '1V']

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for k in range(2,n):
    plt.plot([v/1e-3 for v in vds[k][1:]], [r/1e3 for r in ro[0][k]], '-', label=l[k])
    
ax.set_prop_cycle(None)

for k in range(2,n):
    plt.plot([v/1e-3 for v in vds[k][1:]], [r/1e3 for r in ro[1][k]], ':')  

ax.set_prop_cycle(None)

for k in range(2,n):
    plt.plot([v/1e-3 for v in vds[k][1:]], [r/1e3 for r in ro[2][k]], ':')                                                                                       
                                                                                       
ngl.label_plot(plt_cfg, fig, ax)
plt.savefig('NMOS_ro_corners_2.png', dpi=600)
        
