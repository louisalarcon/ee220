#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:12:08 2020

@author: louis
"""

import matplotlib.pyplot as plt
from si_prefix import si_format

# import our custom ngspice module
import ngspice_link as ngl

# setup the simulation configuration
cfg = {
        'ngspice' : '/Applications/ngspice/bin/ngspice', 
        'cir_dir' : '/Users/louis/Documents/UPEEEI/Classes/EE 220/2020_1/Activities/',
        'cir_file' : 'circuit1.sp',
        }

# create the ngspice object
sim1 = ngl.ngspice(cfg)

# run ngspice with the configuration above
sim1.run_ngspice()

# read the simulation output produced by the 'wrdata' command
vbe, [ic] = sim1.read_dc_analysis('circuit1.dat', [1])

# define the plot parameters
plt_cfg = {
        'grid_linestyle' : 'dotted',
        'title' : r'2N2222a NPN BJT Transfer Characteristics',
        'xlabel' : r'$V_{BE}$ [mV]',
        'ylabel' : r'$I_C$ [mA]',
        'legend_loc' : 'lower left',
        'add_legend' : False,
        'legend_title' : None
        }

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# plot the collector current vs the base-emitter voltage
ax.plot(ngl.scale_vec(vbe, 1e-3), ngl.scale_vec(ic, 1e-3), '-')

# annotate the 1mA point (arbitrary)
ngl.add_hline_text(ax, 1, 550, \
        r'{:.1f} mA'.format(1))

# find the vbe corresponding to 1mA
idx, icx = ngl.find_in_data(ic, 1e-3) 

# annotate the vbe that corresponds to 1mA
ngl.add_vline_text(ax, vbe[idx]/1e-3, 3, r'$V_{BE}=$' + \
        si_format(vbe[idx], precision=2) + 'V')
    
# label the plot
ngl.label_plot(plt_cfg, fig, ax)

# save the plot as an image
plt.savefig('BJT_2n2222a_transfer.png', dpi=600)

