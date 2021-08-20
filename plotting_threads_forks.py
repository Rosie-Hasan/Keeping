
import numpy as np 
import matplotlib 
import matplotlib.pyplot as plt 
import re 
import glob

allocators = ['tc','je','stdc','mi']
colors1 = ['c','dodgerblue','b','midnightblue']
colors2 = ['greenyellow','mediumseagreen','darkgreen','darkslategrey'] 
colors3 = ['orangered','r','firebrick','saddlebrown']
colors4 = ['lightpink','hotpink','m','purple']
y = [1,2,4,8]

for j,k,l,m,n in zip(allocators, colors1, colors2, colors3, colors4):
########
#1 fork
    f4 = [] 
    x = [1,2,4,8] 
    for i in x:
        path = "./{}/1f{}t/timestamps.txt".format(j,i)
        sum = 0 
        events = []
        times = []
        for filename in glob.glob(path):
            with open(filename, 'r') as f:
                for line in f:
                    time = re.findall(r'[\d\.\d]+',line)
                    t = float(time[0])
                    times.append(t)
        #print(times) 
        total = times[1] -times[0]
        #print('1 fork',i,'threds',times[0], times[1],j)#, total  )
        f4.append(100/total) 
    y = [1,2,4,8]
    plt.plot(y ,f4, '--*' ,color='{}'.format(k),  label = '1 fork increasing threading') 
    
    
    ########
    #2 forks 
    f4 = [] 
    x = [1,2,4] 
    for i in x:
        path = "./{}/2f{}t/timestamps.txt".format(j,i)
        sum = 0 
        events = []
        times = []
        for filename in glob.glob(path):
            with open(filename, 'r') as f:
                for line in f:
                    time = re.findall(r'[\d\.\d]+',line)
                    t = float(time[0])
                    times.append(t) 
        total = times[1] -times[0]
        #print('2 forks',i, times, j) 
        f4.append(100/total) 
    y = [2,4,8]
    plt.plot(y, f4, '--*',color='{}'.format(l), label = '2 forks') 
    
    
    
    
    
    ########
    #4 forks 
    f4 = [] 
    x = [1,2] 
    for i in x:
        path = "./{}/4f{}t/timestamps.txt".format(j,i)
        sum = 0 
        events = []
        times = []
        for filename in glob.glob(path):
            with open(filename, 'r') as f:
                for line in f:
                    time = re.findall(r'[\d\.\d]+',line)
                    t = float(time[0])
                    times.append(t) 
        total = times[1] -times[0]
        #print('4 forks',i, times, j)

        f4.append(100/total) 
    y = [4,8]
    plt.plot(y, f4, '--*',color='{}'.format(m), label = '4 forks') 
    
    
    
    
    ########
    #all forks 1 thread  
    f4 = [] 
    x = [1,2,4,8] 
    for i in x:
        path = "./{}/{}f1t/timestamps.txt".format(j,i)
        sum = 0 
        events = []
        times = []
        for filename in glob.glob(path):
            with open(filename, 'r') as f:
                for line in f:
                    time = re.findall(r'[\d\.\d]+',line)
                    t = float(time[0])
                    times.append(t)
        #print('all forks',i, times, j)

        total = times[1] -times[0]
        f4.append(100/total) 
    y = [1,2,4,8]
    plt.plot(y, f4, '--*',color='{}'.format(n), label = 'Increasing forks (1 thread)') 
    
    first_value = f4[0] 
    y = np.array(y)
    z = y * first_value
    plt.plot(y, z, '--k', label = 'Ideal scaling') 
     
    ########
    plt.xlabel('N events (forks * threads) ') 
    plt.ylabel('throughput') 
    plt.ylim(top = 0.9 ) 
    plt.legend()
    plt.title('{}malloc'.format(j))
    plt.savefig("threads_forks_extract_{}.png".format(j))
    plt.clf()     