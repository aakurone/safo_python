#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:53:28 2022

@author: aakurone
"""

import numpy as np
import matplotlib.pyplot as plt



d=np.loadtxt('fort.10')
plt.clf()
plt.imshow(np.log(d))
plt.grid(False)
plt.axis('off')

