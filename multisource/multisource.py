#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:53:28 2022

@author: aakurone
"""

import numpy as np
import matplotlib.pyplot as plt
import multisource_2dmap

func=np.log
cm='summer'
sxmin=-2
sxmax=2
symin=-2
symax=2
xmax=20
n=1000
rmin=0.1
rdep=1

plt.ion()

props=dict(boxstyle='round',edgecolor='white',facecolor='white',alpha=0.9)
fsan=14

for i,d in enumerate(np.linspace(0,10,1001)):
    interf=multisource_2dmap.multisource_2dmap(d,sxmin,sxmax,symin,symax,xmax,n,rmin,rdep)
    plt.clf()
    plt.imshow(func(interf),cmap=cm,vmin=0,vmax=2)
    plt.grid(False)
    plt.axis('off')
    plt.text(50,95,'$d = {:.2f}\, \lambda$'.format(d),usetex=True,fontsize=fsan,bbox=props)
    plt.pause(0.01)
    plt.savefig('frames/{:05d}.png'.format(i))

