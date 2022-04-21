#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:53:28 2022

Plots a 2D map of a collection of radiation sources in a square lattice.
Uses the Fortran subroutine in multisource_2dmap.f90.

Antti Kuronen, 2022, antti.kuronen@helsinki.fi


@author: aakurone
"""

import numpy as np
import matplotlib.pyplot as plt
import multisource_2dmap

func=np.log     # Apply this function to the data before visualization
cm='viridis'    # Color map, try 'jet', 'viridis', 'summer'

sxmin=-2        # Source lattice is [sxmin,symin]×[symin,sxmin] 
sxmax=2         #  with d as the lattice constant
symin=-2
symax=2

xmax=15         # Plot area if [-xmax,xmax]
n=500           # Area is n×n pixels
rmin=0.1        # Skip data if nearer than this to any source
rdep=1          # If rdep>0 include the 1/r dependence to calculations


plt.close('all')
plt.figure(figsize=(8,8))
plt.ion()

#props=dict(boxstyle='square',edgecolor='white',facecolor='white',alpha=0.1)
fsan=16

for i,d in enumerate(np.linspace(0,5,21)):
    interf=multisource_2dmap.multisource_2dmap(d,sxmin,sxmax,symin,symax,xmax,n,rmin,rdep)
    plt.clf()
    plt.imshow(func(interf),cmap=cm,vmin=0,vmax=2)
    plt.grid(False)
    plt.axis('off')
    plt.text(30,55,'$d = {:.2f}\, \lambda$'.format(d),usetex=True,fontsize=fsan,color='white')
    plt.pause(0.01)
    #plt.savefig('frames/{:05d}.png'.format(i))

