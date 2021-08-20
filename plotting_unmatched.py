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

	
	failed_eta = load('failed_eta_{}.npy'.format(o))
	failed_phi = load('failed_phi_{}.npy'.format(o)) 
	failed_z0 = load('failed_z0_{}.npy'.format(o)) 
	failed_pT = load('failed_pT_{}.npy'.format(o)) 
	failed_d0 = load('failed_d0_{}.npy'.format(o)) 
	

	
	
	ax1.hist(failed_eta,bins=50,label='{}'.format(o),alpha=0.2)
	 
	ax2.hist(failed_phi,bins=50,label='{}'.format(o),alpha=0.2)
	
	ax3.hist(failed_z0,bins=200,label='{}'.format(o),alpha=0.2)
	
	ax4.hist(failed_pT,bins=20000,label='{}'.format(o),alpha=0.2)
	
	ax5.hist(failed_d0,bins=100,label='{}'.format(o),alpha=0.2)
	
		
	
ax1.legend() 
ax1.set_ylabel('unmatched') 
ax1.set_xlabel('eta') 	
fig1.suptitle('eta unmatched')
fig1.savefig('eta_inefficiency_test.png') 


ax2.legend() 
ax2.set_ylabel('unmatched') 
ax2.set_xlabel('phi') 	
fig2.suptitle('phi unmatched')
fig2.savefig('phi_inefficiency_test.png') 

ax3.legend() 
ax3.set_ylabel('unmatched') 
ax3.set_xlabel('z0') 	
fig3.suptitle('z0 unmatched')
fig3.savefig('z0_inefficiency_test.png') 

ax4.legend() 
ax4.set_ylabel('umatched') 
ax4.set_xlabel('pT') 	
ax4.set_xlim(-20,20) 
fig4.suptitle('pT unmatched')
fig4.savefig('pT_inefficiency_test.png') 


ax5.legend() 
ax5.set_ylabel('unmatched') 
ax5.set_xlabel('d0') 	
fig5.suptitle('d0 unmatched')
fig5.savefig('d0_inefficiency_test.png') 


