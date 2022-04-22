#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:37:44 2021

@author: aakurone
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('/home/aakurone/Programs/Python/my.mplstyle')

def gauss(x,x0,sigma):
    return np.exp(-(x-x0)**2/(2*sigma**2))

def plot_gaussians(dx):
    lw1=2
    lw2=3
    x=np.linspace(-10,10,1000)
    y1=gauss(x,-dx/2,1)
    y2=gauss(x,dx/2,1)
    y3=y1+y2
    plt.clf()
    plt.plot(x,y1,'r--',linewidth=lw1)
    plt.plot(x,y2,'b--',linewidth=lw1)
    plt.plot(x,y3,'g-',linewidth=lw2)
    

x0=5
sigma=1

x = np.linspace(-10,10,1000)
y1 = gauss(x,-x0,sigma)
y2 = gauss(x,x0,sigma)
y3=y1+y2

plt.ion()

lw1=2
lw2=3
fsan=16

plt.close('all')
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111)
ax.set_ylim(0,2.1)
line1, = ax.plot(x,y1,'r--',linewidth=lw1)
line2, = ax.plot(x,y2,'b--',linewidth=lw1)
line3, = ax.plot(x,y3,'g-',linewidth=lw2)

plt.grid(True)

for dx0 in np.linspace(0,10,1000):
    y1=gauss(x,-x0+dx0,sigma)
    y2=gauss(x,x0-dx0,sigma)
    y3=y1+y2
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    line3.set_ydata(y3)
    fig.canvas.draw()
    fig.canvas.flush_events()

    
