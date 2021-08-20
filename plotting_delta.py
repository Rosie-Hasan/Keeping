import numpy as np 
import matplotlib.pyplot as plt
from numpy import load

fig1 = plt.figure() 


ax1 = fig1.add_subplot(111) 




#label = ['HLTvsOff', 'LRTvsOff', 'HLTvsTruth', 'LRTvsTruth',
label = ['OffvsTruth']


for o in label: 

	
	delta_pT = load('delta_pT_{}.npy'.format(o))
	print(o,min(delta_pT))
	ax1.hist(delta_pT,bins=1000,color='hotpink',label='{}'.format(o),alpha=0.8)#, log = True)
	
	ax1.legend() 
	ax1.set_xlabel('delta pT') 	
	ax1.set_xlim(-1000,1000)
	fig1.suptitle('delta pT')
	fig1.savefig('delta_pT_test_{}.png'.format(o)) 
	plt.cla() 
		
	

