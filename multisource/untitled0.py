#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 14:14:48 2022

@author: aakurone
"""

import numpy as np

def g(r):
    return (-2*np.cos(2*np.pi*r)*np.sin(2*np.pi*r)+np.sin(4*np.pi*r)+4*np.pi)
