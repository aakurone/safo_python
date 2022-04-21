#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:53:28 2022

@author: aakurone
"""

import numpy as np
import matplotlib.pyplot as plt
import doublesource_2dmap

func=lambda x : x #np.log
cm='summer'
xmax=20
n=500
rmin=0.3
rdep=0

props=dict(boxstyle='round',edgecolor='white',facecolor='white',alpha=0.9)
fsan=14

plt.figure(figsize=(9,9))

for d in np.linspace(0,10,201):
    interf=doublesource_2dmap.doublesource_2dmap(d,xmax,n,rmin,rdep)
    plt.clf()
    plt.imshow(interf,cmap=cm)
    plt.grid(False)
    plt.axis('off')
    plt.text(14,35,'$d = {:.2f}\, \lambda$'.format(d),usetex=True,fontsize=fsan,bbox=props)
    plt.pause(0.0001)

plt.pause(5)
    
for d in np.linspace(10,0,201):
    interf=doublesource_2dmap.doublesource_2dmap(d,xmax,n,rmin,rdep)
    plt.clf()
    plt.imshow(interf,cmap=cm)
    plt.grid(False)
    plt.axis('off')
    plt.text(14,35,'$d = {:.2f}\, \lambda$'.format(d),usetex=True,fontsize=fsan,bbox=props)
    plt.pause(0.0001)
    

