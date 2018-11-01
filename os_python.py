# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:48:33 2018

@author: sajid Ullah
"""

import os
curDir=os.getcwd() #know the current working directory
print(curDir)
os.mkdir('Directory') #creating working directory
#os.rename('Directory','NewDirectory') # renaming current directory
print(os.name) #the name of os for module
print(os.path.abspath('.'))
print(os.listdir('.'))