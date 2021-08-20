import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import re
from mpl_toolkits import mplot3d
import glob 


toplot= [] 
forks = [1,2,4,8]
x = [] 
y = [] 
z = [] 

for j in forks: 
   if j == 1: 
      threads = [1,2,4,8]
   if j == 2: 
      threads = [1,2,4]
   if j == 4: 
      threads = [1,2]
   if j == 8: 
      threads = [1]	
   for i in threads:
      times = [] 
      path = "./tc/{}f{}t/timestamps.txt".format(j,i)
      for filename in glob.glob(path):
         with open(filename, 'r') as f:
            for line in f:
              #print(j, 'forks', i, 'threads', line) 
              
               #t = float(time[0])
              times.append(float(line))
            total = times[1] - times[0]
            print(j,'forks', i, 'threads', times, total ) 
            x.append(j) 
            y.append(i) 
            z.append(total)    
print(x,y,z)           
            
            #toplot.append(100/total)
      
            #print(j, 'forks', i, 'threads',  toplot)

x = np.array(x)
y = np.array(y)
z = np.array(z) 
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot3D(x,y,z,'grey')
ax.scatter3D(x,y,z,c=z,cmap = 'spring')
#ax.plot_trisurf(x,y,z,cmap='spring',edgecolor='none') 
#ax.plot(forks,threads,t)
ax.set_xlabel('forks')
ax.set_ylabel('threads')
ax.set_zlabel('time (ms)')
ax.invert_yaxis()


plt.savefig('forks3D.png')
