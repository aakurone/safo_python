#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:37:44 2021

@author: aakurone
"""
import matplotlib.pyplot as plt
import numpy as np


def calc_sw(t,x,n):
    lamb=1
    freq=1
    z1=2*np.pi*x/lamb-2*np.pi*freq*t
    z2=-2*np.pi*x/lamb-2*np.pi*freq*t
    wave1=0
    wave2=0
    for i in range(1,n+1):
        wave1=wave1+1/i*np.sin(i*(2*np.pi*x/lamb-2*np.pi*freq*t))
        wave2=wave2+1/i*np.sin(i*(-2*np.pi*x/lamb-2*np.pi*freq*t))
    y1=np.heaviside(-z1,0.5)*wave1
    y2=np.heaviside(-z2,0.5)*wave2
    return y1+y2

xmax=4
ymax=3

x=np.linspace(-xmax,xmax,1000)
nw=1

plt.ion()
lw=2
plt.close('all')
fig=plt.figure(figsize=(14,8))
ax=fig.add_subplot(111)
ax.set_ylim(-ymax,ymax)
y=calc_sw(0,x,nw)
line1,=ax.plot(x,y,'r-',linewidth=lw)
plt.grid(True)

for t in np.linspace(-xmax,xmax+3.1,1000):
    line1.set_ydata(calc_sw(t,x,nw))
    fig.canvas.draw()
    fig.canvas.flush_events()
    
