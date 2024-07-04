import numpy as np
import scipy as sc
import scipy.constants as spc
import matplotlib.pyplot as plt
import math as m
'''  Program to plot a number of Intensity curves versus Frequency
'''

def stellarIntensity(v,T):
    T1=T
    k1=(2*(spc.h))/((spc.c)**2)
    k2=spc.h/spc.k
    
    I= (k1*(v**3))*(1/(np.exp((k2*v)/T1)-1))
    return I

v= np.linspace(10**12,0.4*10**15,num=10000)
#v= np.arange(10, 10**4, 100)
I1=stellarIntensity(v,500)
I2=stellarIntensity(v,1000)
I3=stellarIntensity(v,1500)

plt.plot(v, I1, color='r', label='500K') 
plt.plot(v, I2, color='g', label='1000K') 
plt.plot(v, I3, color='y', label='1500K')
plt.legend()
plt.xlabel("Frequency ") 
plt.ylabel("Stellar Intensity") 
plt.title("Blackbody body Radiation")
plt.show()