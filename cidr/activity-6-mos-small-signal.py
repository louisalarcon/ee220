#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 13:11:08 2022

@author: louis
"""

import matplotlib.pyplot as plt
import numpy as np

def read_data(data_file, index_list):
    
    sweep_var = []
    data_array = [ [] for i in range(len(index_list)) ]
        
    with open(data_file, 'r') as f:
        for line in f:
            sweep_var.append(float(line.split()[0]))
                
            for idx, val in enumerate(index_list):
                data_array[idx].append(float(line.split()[val]))
                    
    return sweep_var, data_array

corners = ['tt', 'ss', 'ff']
idn = {}
gmn = {}
gmoveridn = {}
vovn = {}

for corner in corners:
    fname = 'mos-nlvt-transfer-' + corner + '-l=150nm-w=10um.dat'
    fdir = '/home/louis/.xschem/simulations/'
    vgs, [idn[corner]] = read_data( fdir + fname, [1])
    gmn[corner] = np.gradient(idn[corner], vgs)
    gmoveridn[corner] = [g/i for g,i in zip(gmn[corner], idn[corner])]
    vovn[corner] = [2*i/g for g,i in zip(gmn[corner], idn[corner])]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for corner in corners:
    ax.plot(vgs, [i/1e-3 for i in idn[corner]], 'o', markersize=1, label = corner.upper())

ax.set_title(r'nfet_01v8_lvt ($W=10\mu m$, $L=0.15\mu m$ )')
ax.set_xlabel(r'$V_{GS}$ [V]')
ax.set_ylabel(r'$I_D$ [mA]')
ax.legend(loc= 'upper left')
fig.set_tight_layout('True')
ax.grid(True)
ax.grid(linestyle=':')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for corner in corners:
    ax.semilogy(vgs, [i/1e-3 for i in idn[corner]], 'o', markersize=1, label = corner.upper())
    
ax.set_title(r'nfet_01v8_lvt ($W=10\mu m$, $L=0.15\mu m$ )')
ax.set_xlabel(r'$V_{GS}$ [V]')
ax.set_ylabel(r'$I_D$ [mA]')
ax.legend(loc= 'upper left')
fig.set_tight_layout('True')
ax.grid(True)
ax.grid(linestyle=':')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for corner in corners:
    ax.plot(vgs, [g/1e-3 for g in gmn[corner]], 'o', markersize=1, label = corner.upper())

ax.set_title(r'nfet_01v8_lvt ($W=10\mu m$, $L=0.15\mu m$ )')
ax.set_xlabel(r'$V_{GS}$ [V]')
ax.set_ylabel(r'$g_m$ [mS]')
ax.legend(loc= 'upper left')
fig.set_tight_layout('True')
ax.grid(True)
ax.grid(linestyle=':')
plt.savefig('nmos-1v8-lvt-gm.png', dpi=600)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for corner in corners:
    ax.plot(vgs, gmoveridn[corner], 'o', markersize=1, label = corner.upper())

ax.set_title(r'nfet_01v8_lvt ($W=10\mu m$, $L=0.15\mu m$ )')
ax.set_xlabel(r'$V_{GS}$ [V]')
ax.set_ylabel(r'$\frac{g_m}{I_D}$ [$V^{-1}$]')
ax.legend(loc= 'upper right')
fig.set_tight_layout('True')
ax.grid(True)
ax.grid(linestyle=':')
plt.savefig('nmos-1v8-lvt-gmoverid.png', dpi=600)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for corner in corners:
    ax.plot(vgs, vovn[corner], 'o', markersize=1, label = corner.upper())

ax.set_title(r'nfet_01v8_lvt ($W=10\mu m$, $L=0.15\mu m$ )')
ax.set_xlabel(r'$V_{GS}$ [V]')
ax.set_ylabel(r'$V_{ov} = \frac{2 \cdot I_D}{g_m}$ [$V^{-1}$]')
ax.legend(loc= 'upper left')
fig.set_tight_layout('True')
ax.grid(True)
ax.grid(linestyle=':')

ft = {}
for corner in corners:
    fname = 'mos-ft-' + corner + '-l=150nm-w=10um.dat'
    fdir = '/home/louis/.xschem/simulations/'
    vgs, [ft[corner]] = read_data( fdir + fname, [1])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for corner in corners:
    ax.plot(vgs, [f/1e9 for f in ft[corner]], 'o', markersize=1, label = corner.upper())

ax.set_title(r'nfet_01v8_lvt ($W=10\mu m$, $L=0.15\mu m$ )')
ax.set_xlabel(r'$V_{GS}$ [V]')
ax.set_ylabel(r'$f_T$ [GHz]')
ax.legend(loc= 'upper left')
fig.set_tight_layout('True')
ax.grid(True)
ax.grid(linestyle=':')

ftgmoveridn = {}
for corner in corners:
    ftgmoveridn[corner] = [f*g for f,g in zip(ft[corner], gmoveridn[corner])]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for corner in corners:
    ax.plot(vgs, [x/1e9 for x in ftgmoveridn[corner]], 'o', markersize=1, label = corner.upper())

ax.set_title(r'nfet_01v8_lvt ($W=10\mu m$, $L=0.15\mu m$ )')
ax.set_xlabel(r'$V_{GS}$ [V]')
ax.set_ylabel(r'$f_T\cdot \frac{g_m}{I_D}$ [$\frac{GHz}{V}$]')
ax.legend(loc= 'upper right')
fig.set_tight_layout('True')
ax.grid(True)
ax.grid(linestyle=':')
plt.savefig('nmos-1v8-lvt-ftgmoverid.png', dpi=600)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for corner in corners:
    ax.plot(vovn[corner], [x/1e9 for x in ftgmoveridn[corner]], 'o', markersize=1, label = corner.upper())

ax.set_title(r'nfet_01v8_lvt ($W=10\mu m$, $L=0.15\mu m$ )')
ax.set_xlabel(r'$V_{ov}=\frac{2\cdot I_D}{g_m}$ [V]')
ax.set_ylabel(r'$f_T\cdot \frac{g_m}{I_D}$ [$\frac{GHz}{V}$]')
ax.legend(loc= 'upper right')
fig.set_tight_layout('True')
ax.grid(True)
ax.grid(linestyle=':')
plt.savefig('nmos-1v8-lvt-ftgmoverid-vs-vov.png', dpi=600)

idn2 = {}
gdsn = {}
ron = {}
for corner in corners:
    fname = 'mos-nlvt-output-' + corner + '-l=150nm-w=10um-vgs=0.9v.dat'
    fdir = '/home/louis/.xschem/simulations/'
    vds, [idn2[corner]] = read_data( fdir + fname, [1])
    gdsn[corner] = np.gradient(idn2[corner], vds)
    ron[corner] = [1/g for g in gdsn[corner]]
    
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for corner in corners:
    ax.plot(vds, [i/1e-3 for i in idn2[corner]], 'o', markersize=1, label = corner.upper())

ax.set_title(r'nfet_01v8_lvt ($W=10\mu m$, $L=0.15\mu m$ )')
ax.set_xlabel(r'$V_{DS}$ [V]')
ax.set_ylabel(r'$I_D$ [mA]')
ax.legend(loc= 'upper left')
fig.set_tight_layout('True')
ax.grid(True)
ax.grid(linestyle=':')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for corner in corners:
    ax.plot(vds, [r/1e3 for r in ron[corner]], 'o', markersize=1, label = corner.upper())

ax.set_title(r'nfet_01v8_lvt ($W=10\mu m$, $L=0.15\mu m$ )')
ax.set_xlabel(r'$V_{DS}$ [V]')
ax.set_ylabel(r'$r_o$ [$k\Omega$]')
ax.legend(loc= 'upper left')
fig.set_tight_layout('True')
ax.grid(True)
ax.grid(linestyle=':')
plt.savefig('nmos-1v8-lvt-ro.png', dpi=600)
