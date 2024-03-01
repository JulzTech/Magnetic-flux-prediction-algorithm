# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 18:17:30 2023

@author: julsi
"""

import matplotlib.pyplot as plt


import sunpy.coordinates  # NOQA
import sunpy.map

import glob 

import pandas as pd

import numpy as np

from scipy.fft import fft, fftfreq


files =glob.glob('C:/Users/.../**.fits')

coaligned_mc = sunpy.map.Map(files, sequence=True)

#coaligned_mc[0].peek()



    
x = list(range(500, 540))
y = list(range(500, 540))

#G = 5


#s = random.choices(x, k=G)
#d = random.choices(y, k=G)


    
    
coor0 = []
for j in x:
        
        x1 = j 
        
        #print(x1)
        for h in y:
    
            y1 = h
        
        #print(y1)
    
            c = (y1,x1)
        
            coor0.append(c)
            
#coor = random.choices(coor0, k=G)

q = len(coor0)

hj = len(coaligned_mc)

  
files1 =[]



for i, map in enumerate(coaligned_mc):
    data = map.data
    
    
    
    for y in range(q):
    
        data1 = data[coor0[y]]
        print(coor0[y])
        
        
        
        files1.append(data1)
        
        
    
plt.imshow(data, origin = "lower")
plt.scatter(x1,y1)
plt.show()
#        
    
        
filesarr = np.array(files1, dtype = object)



weee = np.resize(filesarr, (hj,q))


files2 = []


for element in filesarr:
    if str(element) != "nan":
        files2.append(element)
    
N00 = len(coaligned_mc)

N0 = (len(files1) - len(files2))/q

N = N00 - int(N0)


we = np.resize(files2, (hj,q))  

we0 = np.delete(we,slice(N,N00,1) , axis=0)

window = np.hamming(N)


def X_norm(iterable):
    return ((iterable) - (iterable).mean()) / ((iterable).mean())

def geomean(iterable):
     return np.exp(np.log(iterable).mean())
    



df = pd.DataFrame(we0)



zzz = []

for i in range(q):
    x00 = we0[:,i]
    
    #x11 = np.reshape([x00], (N,1))
    x12 = pd.DataFrame(x00)
    x13 = x12.mean()
    x14 = ((x12) - (x13)) / (x13)
    #zz = X_norm(x11)
    
    x15 =np.reshape([x14], (1,N))
    
    
    z00 = x15*window
    
    
    fftt = fft(z00)
    
    zzz.append(fftt)


k = np.reshape([zzz], (q,N))

df11 = pd.DataFrame(k)

lol = geomean(df11)




T = 12




yf1 = np.reshape([lol], (N,1))


xf = fftfreq(N, T)[:N//2]




plt.yscale("log")
plt.xscale("log")
#plt.yscale("freq")
plt.title('Sun Spot')
plt.xlabel('Frequency (mHz)')
plt.ylabel('Arb. Units')
plt.plot(xf*1e3, 2.0/N * np.abs(yf1[0:N//2]))



plt.show()

#pdb.set_trace()
