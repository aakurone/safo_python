#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:37:44 2021

@author: aakurone
"""
import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(0,15,1000)
y1 = np.sin(x)
y2 = np.sin(x+0)
y3=y1+y2

plt.ion()

lw1=1.5
lw2=4

fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111)
ax.set_ylim(-2.1,2.1)
line1, = ax.plot(x,y1,'r-',linewidth=lw1)
line2, = ax.plot(x,y2,'b-',linewidth=lw1)
line3, = ax.plot(x,y3,'g-',linewidth=lw2)

plt.grid()

for phi in np.linspace(0,4.1*np.pi,800):
    line1.set_ydata(np.sin(x))
    line2.set_ydata(np.sin(x+phi))
    line3.set_ydata(np.sin(x)+np.sin(x+phi))
    fig.canvas.draw()
    fig.canvas.flush_events()
    
