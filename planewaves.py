#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:55:21 2022

Plot the interference pattern from planewaves. 
For details, see planewaves.f90 that has the module
source code.

@author: aakurone, antti.kuronen@helsinki.fi
"""

import numpy as np
import matplotlib.pyplot as plt
import planewaves

def plot_planewaves(xmax=50,nw=5,k=1,n=1000,savefig=False,cmap='jet'):
    a=planewaves.planewaves(xmax,nw,k,n)
    plt.clf()
    plt.imshow(np.real(a),cmap=cmap)
    plt.grid(False)
    plt.axis('off')
    props=dict(boxstyle='round',edgecolor='w',facecolor='w',alpha=1)
    plt.text(n/30,n/17,'$n_\mathrm{}w{}={:d}$'.format('{','}',nw),usetex=True,fontsize=16,bbox=props)
    if savefig: 
        plt.savefig('planewaves_{:04d}.png'.format(nw))


if __name__=='__main__':
    for nw in range(2,10):
        plot_planewaves(xmax=100,nw=nw,n=1000,savefig=False)
        plt.pause(2)

    
