import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime 
from numpy import save

HLT_dict = np.load('HLT_dict.npy', allow_pickle='TRUE').item() 
LRT_dict = np.load('LRT_dict.npy', allow_pickle='TRUE').item()
Offline_dict = np.load('Offline_dict.npy', allow_pickle='TRUE').item()
Truth_dict = np.load('Truth_dict.npy', allow_pickle='TRUE').item()
ROI_dict = np.load('ROI_dict.npy', allow_pickle='TRUE').item()


ROIkey = ROI_dict.keys() 

def ROI(r,name1, a, name2,b): 
    compareto_dict = {} 
    compare_dict = {} 
    
    eta_min = ROI_dict[r][0]
    eta_max = ROI_dict[r][1]
    #print(eta_min,eta_max)  
    
    for i in b: 
    		
    
        
    	if name2[i][5] == r and name2[i][0] > eta_min and name2[i][0] < eta_max:
           	compareto_dict[i] = name2[i] 
    
    for j in a:        
    	if name1[j][5] == r:
        	   compare_dict[j] = name1[j]        
      

    #print(compareto_dict) 
    return compareto_dict, compare_dict
     


def match(a,d): 
    
         
           match = False 	
           delta_eta = abs(compare_dict[a][0] - compareto_dict[d][0])    	
    	
           if delta_eta < 0.1: 
           	match = True 
           else:
           	return False 
    	
           delta_phi = abs(compare_dict[a][1] - compareto_dict[d][1])
           if delta_phi < 0.1:
           	match = True
                
        	
           else:
           	return False 
       
           return match     
    
  


####### comparing tracks 
HLTkey = HLT_dict.keys() 
LRTkey = LRT_dict.keys() 
Offkey = Offline_dict.keys()
Truthkey = Truth_dict.keys()  

total_matches = 0 
total_failed = 0 


first = [HLTkey, LRTkey, HLTkey, LRTkey]
second = [Offkey, Offkey, Truthkey, Truthkey] 
third = [HLT_dict, LRT_dict, HLT_dict, LRT_dict]
fourth = [Offline_dict, Offline_dict, Truth_dict, Truth_dict] 
label = ['HLTvsOff', 'LRTvsOff', 'HLTvsTruth', 'LRTvsTruth']



#####track.eta, track.phi, track.z0, track.pT, track.d0]

for k,l,m,n,o in zip(first, second, third, fourth, label): 
	

	
	
	failed_eta = []
	failed_phi = [] 
	failed_z0 = [] 
	failed_pT = [] 
	failed_d0 = [] 
	eta = []
	phi = []
	z0 = [] 
	pT = [] 
	d0 = [] 
	total_eta = [] 
	total_phi = [] 
	total_z0 = [] 
	total_pT = [] 
	total_d0 = [] 
	delta_pT = [] 
	total_matches = 0 
	total_failed = 0 
	matched = False
	
	start = datetime.now().time() 
	for r in ROIkey:
		
	
		#for i,j in zip(k,l): 
			#print(r) 
		compareto_dict, compare_dict = ROI(r,m,k,n,l) 
			#print(j,compareto_dict,i,compare_dict) 
		#print('comparing', len(compare_dict.keys()), 'compare to', len(compareto_dict.keys()))
		 
		for a in compare_dict.keys(): 
			for d in compareto_dict.keys():   
				if match(a,d):  
					#total_matches = total_matches + 1 
					#print('match') 	
        	   	
					matched = True 
					break 
				else: 
					#total_failed = total_failed + 1 
					matched = False	
					#print('failed') 
			if matched == True: 
				total_matches = total_matches + 1 
				delta_pT.append(m[a][3]-n[d][3])
				eta.append(m[a][0]) 
				phi.append(m[a][1]) 
				z0.append(m[a][2]) 
				pT.append(m[a][3])
				d0.append(m[a][4]) 
			else: 
				total_failed = total_failed + 1 
        	
				failed_eta.append(m[a][0])
				failed_phi.append(m[a][1])
				failed_z0.append(m[a][2]) 
				failed_pT.append(m[a][3])
				failed_d0.append(m[a][4])
		#print('per event','matched=',total_matches, 'failed', total_failed) 
	
	 
	
		 
		
		    
	
	end = datetime.now().time() 

	print('start=', start, 'end=', end) 
	  
	total_eta = eta + failed_eta  
	total_phi = phi + failed_phi 
	total_z0 = z0 + failed_z0 
	total_pT = pT + failed_pT 
	total_d0 = d0 + failed_d0 
        	    
##### saving arrays 
	save('eta_{}.npy'.format(o),eta) 
	save('failed_eta_{}.npy'.format(o),failed_eta) 
	save('total_eta_{}.npy'.format(o),total_eta) 
	save('phi_{}.npy'.format(o),phi) 
	save('failed_phi_{}.npy'.format(o),failed_phi) 
	save('total_phi_{}.npy'.format(o),total_phi)
	save('z0_{}.npy'.format(o),z0) 
	save('failed_z0_{}.npy'.format(o),failed_z0) 
	save('total_z0_{}.npy'.format(o),total_z0)
	save('pT_{}.npy'.format(o),pT) 
	save('failed_pT_{}.npy'.format(o),failed_pT) 
	save('total_pT_{}.npy'.format(o),total_pT)
	save('d0_{}.npy'.format(o),d0) 
	save('failed_d0_{}.npy'.format(o),failed_d0) 
	save('total_d0_{}.npy'.format(o),total_d0)
	save('delta_pT_{}'.format(o),delta_pT)
	    



def match2(a,b):

    match = False 

    
    

    delta_eta = abs(Truth_dict[a][0] - Offline_dict[b][0])    	
    	
    if delta_eta < 0.01: 
        match = True 
    else:
        return False 
    
    delta_phi = abs(Truth_dict[a][1] - Offline_dict[b][1])
    if delta_phi < 0.01:
        match = True
        
    else:
        return False 
        
    #same_event = name1[stra][5] - name2[strb][5] 
    #if same_event == 0: 
    #	match = True 
    #else: 
    #	return False 
    return match 
    
     
 
	
failed_eta = []
failed_phi = [] 
failed_z0 = [] 
failed_pT = [] 
failed_d0 = [] 
eta = []
phi = []
z0 = [] 
pT = [] 
d0 = [] 
total_eta = [] 
total_phi = [] 
total_z0 = [] 
total_pT = [] 
total_d0 = [] 
delta_pT = []
total_matches = 0 
total_failed = 0 
matched = False

start = datetime.now().time() 
  
for x in Offkey: 
    for y in Truthkey: 
       	if match2(y,x):
        
       	    total_matches = total_matches + 1 
       	    
       	    matched = True 
       	    break 
       	else: 
       	    total_failed = total_failed + 1 
       	    matched = False	
    if matched == True: 
        	
        delta_pT.append(Offline_dict[x][3]-Truth_dict[y][3])	
        eta.append(Offline_dict[x][0]) 
       	phi.append(Offline_dict[x][1]) 
       	z0.append(Offline_dict[x][2]) 
       	pT.append(Offline_dict[x][3])
       	d0.append(Offline_dict[x][4]) 
    else: 
        	
       	failed_eta.append(Offline_dict[x][0])
       	failed_phi.append(Offline_dict[x][1])
       	failed_z0.append(Offline_dict[x][2]) 
       	failed_pT.append(Offline_dict[x][3])
       	failed_d0.append(Offline_dict[x][4])
#
end = datetime.now().time() 
#                                            	  
print('start=', start, 'end=', end) 

total_eta = eta + failed_eta  

total_phi = phi + failed_phi 
total_z0 = z0 + failed_z0 
total_pT = pT + failed_pT 
total_d0 = d0 + failed_d0 


##### saving arrays 
save('eta_OffvsTruth.npy',eta) 
save('failed_eta_OffvsTruth.npy',failed_eta) 
save('total_eta_OffvsTruth.npy',total_eta) 
save('phi_OffvsTruth.npy',phi) 
save('failed_phi_OffvsTruth.npy',failed_phi) 
save('total_phi_OffvsTruth.npy',total_phi)
save('z0_OffvsTruth.npy',z0) 
save('failed_z0_OffvsTruth.npy',failed_z0) 
save('total_z0_OffvsTruth.npy',total_z0)
save('pT_OffvsTruth.npy',pT) 
save('failed_pT_OffvsTruth.npy',failed_pT) 
save('total_pT_OffvsTruth.npy',total_pT)
save('d0_OffvsTruth.npy',d0) 
save('failed_d0_OffvsTruth.npy',failed_d0) 
save('total_d0_OffvsTruth.npy',total_d0)
save('delta_pT_OffvsTruth',delta_pT)

print('arrays all done') 

