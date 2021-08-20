import numpy as np 
import matplotlib.pyplot as plt
from numpy import load


fig1 = plt.figure() 
fig2 = plt.figure() 
fig3 = plt.figure() 
fig4 = plt.figure() 
fig5 = plt.figure() 
fig6 = plt.figure()

ax1 = fig1.add_subplot(111) 
ax2 = fig2.add_subplot(111) 
ax3 = fig3.add_subplot(111)
ax4 = fig4.add_subplot(111)
ax5 = fig5.add_subplot(111)
ax6 = fig6.add_subplot(111)



label = ['HLTvsOff', 'LRTvsOff', 'HLTvsTruth', 'LRTvsTruth','OffvsTruth']


for o in label: 

	
	
	eta = load('eta_{}.npy'.format(o))
	phi = load('phi_{}.npy'.format(o))
	z0 = load('z0_{}.npy'.format(o)) 
	pT = load('pT_{}.npy'.format(o)) 
	d0 = load('d0_{}.npy'.format(o)) 
	total_eta = load('total_eta_{}.npy'.format(o)) 
	total_phi = load('total_phi_{}.npy'.format(o)) 
	total_z0 = load('total_z0_{}.npy'.format(o)) 
	total_pT = load('total_pT_{}.npy'.format(o)) 
	total_d0 = load('total_d0_{}.npy'.format(o))
	
	

	
	ns = [0,0]
	ns, bins, patches = ax1.hist([eta,total_eta],bins=10,color=['m','c'],label=['matched','total'],alpha=0.2)
	 
	ax2.plot(bins[:-1], np.divide(ns[0],ns[1], out=np.zeros_like(ns[0]),where=ns[1]!=0),marker='*',linestyle='--',label='{}'.format(o)) 
	
	
	ns = [0,0]
	ns, bins, patches = ax1.hist([phi,total_phi],bins=10,color=['m','c'],label=['matched','total'],alpha=0.2)
	ax3.plot(bins[:-1], np.divide(ns[0],ns[1], out=np.zeros_like(ns[0]),where=ns[1]!=0),marker='*',linestyle='--',label='{}'.format(o)) 
	

	ns, bins, patches = ax1.hist([z0,total_z0],bins=10,color=['m','c'],label=['matched','total'],alpha=0.2)
	ax4.plot(bins[:-1], np.divide(ns[0],ns[1], out=np.zeros_like(ns[0]),where=ns[1]!=0),marker='*',linestyle='--',label='{}'.format(o)) 
	
	ns = [0,0]
	ns, bins, patches = ax1.hist([pT,total_pT],bins=10,color=['m','c'],label=['matched','total'],alpha=0.2)
	#ax5.plot(bins[:-1], np.divide(ns[0],ns[1], out=np.zeros_like(ns[0]),where=ns[1]!=0),marker='*',linestyle='--',label='{}'.format(o))
	ratio = np.divide(ns[0],ns[1], out=np.zeros_like(ns[0]),where=ns[1]!=0)
	values = np.array(ratio) 
	values[ values==0] = np.nan 	
	ax5.plot(bins[:-1], values,marker='*',linestyle='--',label='{}'.format(o)) 
	
	ns = [0,0]
	ns, bins, patches = ax1.hist([d0,total_d0],bins=10,color=['m','c'],label=['matched','total'],alpha=0.2)
	ax6.plot(bins[:-1], np.divide(ns[0],ns[1], out=np.zeros_like(ns[0]),where=ns[1]!=0),marker='*',linestyle='--',label='{}'.format(o)) 
	




	
	
ax2.legend() 
ax2.set_ylabel('efficiency') 
ax2.set_xlabel('eta') 	
fig2.suptitle('eta efficiency')
fig2.savefig('eta_efficiency_test.png') 


ax3.legend() 
ax3.set_ylabel('efficiency') 
ax3.set_xlabel('phi') 	
fig3.suptitle('phi efficiency')
fig3.savefig('phi_efficiency_test.png') 

ax4.legend() 
ax4.set_ylabel('efficiency') 
ax4.set_xlabel('z0') 	
fig4.suptitle('z0 efficiency')
fig4.savefig('z0_efficiency_test.png') 

ax5.legend() 
ax5.set_ylabel('efficiency') 
ax5.set_xlabel('pT') 	
fig5.suptitle('pT efficiency')
fig5.savefig('pT_efficiency_test.png') 


ax6.legend() 
ax6.set_ylabel('efficiency') 
ax6.set_xlabel('d0') 	
fig6.suptitle('d0 efficiency')
fig6.savefig('d0_efficiency_test.png') 


