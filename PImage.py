# -*- coding: utf-8 -*-
# PImage.py
"""
Created on Wed Mar 8, 2017

@author: bgoldfeder
"""

import os,sys
import numpy as np
import scipy.misc as sm
import scipy.ndimage as nd
import scipy.signal as sg

class PImage:

    def __init__(self,fname):
        self.fname = fname
        self.orig = sm.imread(fname)
        self.finalImg = np.copy(self.orig)
        self.steps = []
        print("made a PImage")

    def Process(self,steps):
        N = len(steps)
        for command in steps:
            cName = command[0]
            if (cName == "D"):
                print("in Shift")
                yIn = command[1]
                xIn = command[2]
                vec = np.array([ yIn,xIn ])
                self.finalImg = nd.shift(self.finalImg,vec)
            elif (cName == "R"):
                print("in Rotate")
                deg = command[1]
                self.finalImg = nd.rotate(self.finalImg,deg)
                
            elif (cName == "C"):
                print("in Crop")
                top = command[1]
                bottom = command[2]
                left = command[3]
                right = command[4]
                self.finalImg = self.finalImg[top:bottom, left:right]
                
            elif (cName == "S"):
                print("in Smooth")
                smooth = command[1]
                self.finalImg = sg.cspline2d(self.finalImg,smooth)
            elif (cName == "L"):
                print("in Dilation")
                dil = command[1]
                self.finalImg = nd.grey_dilation(self.finalImg,dil)
            elif (cName == "T"):
                print("in Square Root")
                self.finalImg = np.sqrt(self.finalImg)
            elif (cName == "P"):
                print("in Passive Threshold")
                thresh = command[1]
                lowValIndic = self.finalImg < thresh
                self.finalImg[lowValIndic] = 0 
        sm.imsave("finalImag.jpg",self.finalImg)
            

 
