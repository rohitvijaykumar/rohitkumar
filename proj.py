# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 12:12:15 2016

@author: Rohit
"""

import scipy,numpy
import scipy.optimize, scipy.stats
import numpy.random

import statsmodels
import statsmodels.stats
import statsmodels.stats.stattools as stools


print("Is the flow radial or axial?")
flow=input("Enter 1 for radial , 2 for axial ")

vol=input("Please enter the volume of the reactor in m3 ")
rev=input("Please enter the speed of rotation in rps ")
Pon=input("Please enter the power number of system ")
ro=input("Please enter the density of the liquid ")

# For the given data we find all dimensions of stirrer
# This is done in such a way as to have minimum power consumption
# for constant rpm and density for min power diameter of impeller minimum

# 0.2 <= D/T <= 0.5
# 0.5 <= H/T <= 1
# 0.1 <= C/T <= 0.3
# 1/12 <= B/T <= 1/10

# For min D for fixed T, D/T=0.2 i.e D = 0.2 T
# Similarly C= 0.1 T and B= T/12
# D/T is fixed so id D is minimum T is minimum
# This makes H/T maximum. H/T max= 1 so H = T

T=(vol*4*7/22)**(0.3333333)
H=T
D=0.2*T
C=0.1*T
B=T/12
print("For minimum power consumption- ")

print("Height of Liq in Vessel(in m)- ")
print(H)
print("Diameter of Impeller in Vessel(in m)- ")
print(D)
print("Diameter of Vessel(in m)- ")
print(T)
print("Clearance Height(in m) - ")
print(C)
print("Baffle Width(in m)- ")
print(B)

W= D/5 # Standard practice

print("Width of impeller(in m)- ")
print W

DD=D*D*D*D*D
P=Pon*ro*rev*rev*rev*DD
Puv=(P*4*7)/(22*T*T*H)
Torque=(P*7)/(22*2*rev)

print(" Minimum Power consumed(in J/s)- ")
print P
print(" Minimum Power consumed per unit vol(J/m3/s)- ")
print Puv
print(" Torque acting(J)- ")
print Torque

x=D/T


vc=0.53*(Pon)**(1/3)*rev*D*(D/W)*(D/T)**(7/6)
print(" Circulation velocity(m/s)- ")
print vc

if flow==1:
    lloop=2*(H-C)+T #length of longest loop
    ctime=lloop/vc
    mixtime=5*ctime
    BlendNo=rev*mixtime
    
    print("length of longest loop for radial flow is(in m) ")
    print lloop
    print("The circulation time in longest loop is(sec) ")
    print ctime
    print("The mixing time for the vessel is(sec) ")
    print mixtime
    print("The Blend Number for the vessel is ")
    print BlendNo
   
if flow==2:
    lloop=2*H+T #length of longest loop
    ctime=lloop/vc
    mixtime=5*ctime
    BlendNo=rev*mixtime
    
    print("length of longest loop for axial flow is(in m) ")
    print lloop
    print("The circulation time in longest loop is(sec) ")
    print ctime
    print("The mixing time for the vessel is(sec) ")
    print mixtime
    print("The Blend Number for the vessel is ")
    print BlendNo
    
    