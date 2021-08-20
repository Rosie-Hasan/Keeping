import numpy as np 
import matplotlib 
import matplotlib.pyplot as plt 
import re 
import glob
import pandas as pd 


forks = [1,2,4]
x1 = [1,2,4,8]
x2 = [2,4,8]
x4 = [4,8]
xs = [x1,x2,x4]
allocators = ['tc','je','stdc','mi']
colors1 = ['c','dodgerblue','b','midnightblue']
colors2 = ['greenyellow','mediumseagreen','darkgreen','darkslategrey']
colors3 = ['orangered','r','firebrick','saddlebrown']
colors4 = ['lightpink','hotpink','m','purple']
colors = [colors1, colors2, colors3] 


for f,x,z in zip(forks,xs,colors):  
    colours = z 

    for j,k in zip(allocators, colours):
    
    #for loop for forks f 
    #for loop for allocators j  
    #for loop for threads k 
    
    
    #1 fork
        x = x
        array= []
        path = "./{}/{}f*t/prmon.athenaHLT.txt".format(j,f)
        for filename in glob.glob(path):  
            text = pd.read_csv(filename, delimiter='\t')   
            y1 = text["pss"] *1e-6   
            memory1 =  np.amax(y1) 
    	#mean1 = memory1/time1
    	#print("one thread:", "time=",time1,"memory=", memory1,"mean=", mean1)   
            array.append(memory1) 
        print(array, x, j,f ) 
        plt.plot(x, array,'--*', color = "{}".format(k), label = "{}".format(j))
        plt.xlabel('Threads') 
        plt.ylabel('peak pss (GB)')
        plt.title('{} forks'.format(f))  
        plt.legend()
        first_value = array[0]
    #print(first_value)
    x = np.array(x) 
    y = x * first_value 
    #print(x,y)   
    plt.plot(x,y, '--k', label = 'ideal scaling') 
    plt.savefig("peakpss_{}_forks_scaling".format(f))
    plt.clf()


for j,k in zip(allocators, colors4):

   #all fork
    x=x1   
    array= []
    path = "./{}/*f1t/prmon.athenaHLT.txt".format(j)
    for filename in glob.glob(path):
        text = pd.read_csv(filename, delimiter='\t')
        y1 = text["pss"] *1e-6 
        memory1 =  np.amax(y1)
       #mean1 = memory1/time1
       #print("one thread:", "time=",time1,"memory=", memory1,"mean=", mean1)
        array.append(memory1)
   #print(array, j )
    plt.plot(x, array,'--*', color = "{}".format(k), label = "{}".format(j))
    first_ = array[0]
   #y = first * x
   #plt.plot(x,y, '--k', label = 'ideal scaling')

    plt.xlabel('N events (forks * threads)')
    plt.ylabel('peak pss (GB)')
    plt.title('all forks')
    plt.legend()
plt.savefig("peakpss_all_forks_best".format(f))
plt.clf()


 