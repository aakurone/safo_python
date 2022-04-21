#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:37:44 2021

@author: aakurone
"""
import matplotlib.pyplot as plt
import numpy as np


def gaussian_pulse(x,t,k,c,sigma):
    return np.exp(-(k*x-c*t)**2/2/sigma**2)*np.sin(k*x-c*t)

def gaussian(x,t,k,c,sigma):
    return np.exp(-(k*x-c*t)**2/2/sigma**2)


k=10
sigma=5
c=5

x = np.linspace(0,15,1000)
y = gaussian_pulse(x,0,k,c,sigma)
yg = gaussian(x,0,k,c,sigma)

plt.ion()

fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot(111)
ax.set_ylim(-1,1)
line1, = ax.plot(x,y,'r-')
line2, = ax.plot(x,yg,'b-',linewidth=0.4)

plt.grid()

for t in np.linspace(0,40,400):
    line1.set_ydata(gaussian_pulse(x,t,k,c,sigma))
    line2.set_ydata(gaussian(x,t,k,c,sigma))
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.001)
    
