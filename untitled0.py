#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:39:58 2022

@author: aakurone
"""

import multisource_2dmap
import numpy as np
import matplotlib.pyplot as plt


d=multisource_2dmap.multisource_2dmap(1,1,20,1001,0.01,False)
plt.clf(); plt.imshow(d); plt.grid(False)