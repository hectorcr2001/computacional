# -*- coding: utf-8 -*-
"""problema2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nz2IUr_8K_KVlnhA9Wg6Y6chBT3c14C2

a)T=0-0,5
b)T=4,5-5
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import random as randomp
from random import seed
from random import random
from datetime import datetime

l=100 #numero iteraciones
now = datetime.now()
seed(now.microsecond)
#paso 0 (inicializar)
t=5
npart=100
s=randomp.choice([1,-1],size=(npart+1,npart+1))

f = open("ising_data.dat", "w")

for i in range(l):
  n = randomp.randint(npart)
  m = randomp.randint(npart)

  #print(n," ",m)
  #condiciones de contorno
  s[0]=s[npart-1]
  s[npart]=s[1]
  s[:,0]=s[:,npart-1]
  s[:,npart]=s[:1]
  

  #print(s)
  p=min(1,math.exp((2*s[n][m])*(s[n+1][m]+s[n-1][m]+s[n][m+1]+s[n][m-1])/t))
  #print(p)
  #generamos numero aleatorio
  xi=random()
  if(xi<p):
    s[n][m]=-s[n][m]

  for j in range(npart):
    for k in range(npart):
      print(s[j][k],", ",end="", file=f)
    
  print("\n",file=f)
  
  #print(s)

f.close()

