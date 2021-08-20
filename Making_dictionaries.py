#######ng class 
import numpy as np 

class Track:
    def __init__(self):
        self.name = 0  
        self.eta = 0 
        self.phi = 0
        self.z0 = 0
        self.d0 = 0
        self.pT = 0
        self.event = 0
        self.hp = 0  

####### splitting offline and HLT
start = ['Offline', 'HLT', 'LRT']
ends = ['HLT', 'LRT','HLT']

Offline_dict = {}
HLT_dict = {} 
LRT_dict = {}


for k,l in zip(start, ends): 
	####### making tracks  
	is_track = False 
	copy = False 
	new_event = False 
	k_dict = {} 
	
	import csv 
	
	with open('test_file1', newline='') as csvfile:
		new_reader = csv.reader(csvfile, delimiter='\t')
		for row in new_reader:
			for i in range(1,len(row)): # seperate offline, HLT, LRT 
	              		fullstring = row[i]
	              		substring = "event" 
	              		if substring in fullstring: 
	               			event_no = row[i]
	               			new_event = False  
	               			#print(event_no)   
	              		else: 
	               			new_event = True  
	              		fullstring = row[i]
	              		substring = k
	              		substring2 = l 
	              		substring3 = 'Truth'
	              		if new_event == True: 
	              			
	              			if k == 'LRT': 
	              				if substring in fullstring and substring2 in fullstring: 
	                				copy = True 
	              				if substring2 in fullstring and substring not in fullstring:
	                				copy = False 
	              				if substring3 in fullstring:
	              					copy = False 
	              		
	              				
	              			else: 
	              				if substring in fullstring: 
	                				copy = True 
	              				if substring2 in fullstring:
	                				copy = False
	              				if substring3 in fullstring:
	                				copy = False     			
	   
                            
			if copy == True:         	
	              		
	              		for i in range(1,len(row)): # seperate chain line and tracks 
	                		
	                		fullstring = row[i]
	                		substring = "Chain" 
	                		if substring in fullstring: 
	                			chain_name = row   
	                			is_track = False 
	                		else: 
	                			is_track = True   
	              		if is_track == True: 
	                		#print(event_no) 
	                		track = Track() # make track and fill it 
	                		
	                		if len(row)>5:    
	                			 
	                			track.event = float(event_no.replace("event:",""))
	                			#print(k,len(row)) 
	                			fullstring = row[4]
	                			substring = "eta" 
	                			if substring in fullstring:
	                				track.eta = float(row[4].replace("eta=",""))
	                			fullstring = row[5]
	                			substring = "phi"
	                			if substring in fullstring:
	                				track.phi = float(row[5].replace("phi=",""))
	                			fullstring = row[6]
	                			substring = "z0" 
	                			if substring in fullstring:
	                				track.z0 = float(row[6].replace("z0=",""))
	                			fullstring = row[7]
	                			substring = "pT" 
	                			if substring in fullstring:
	                				track.pT = float(row[7].replace("pT=","").replace("GeV",""))
	                			fullstring = row[8]
	                			substring = "d0" 
	                			if substring in fullstring:
	                				track.d0 = float(row[8].replace("d0=",""))
	                			fullstring = row[9]
	                			substring = "hp" 
	                			if substring in fullstring:
	                				track.hp = row[9].replace("hp=","")
	                			fullstring = row[13]
	                			substring = "id" 
	                			if substring in fullstring:
	                				ID = row[13]
	                			track.name = chain_name[1] + ' ' + ID + event_no
	                			####### add track to directory 
	                			if k == 'LRT': 
	                				LRT_dict [track.name] = [track.eta, track.phi, track.z0, track.pT,track.d0,track.event,track.hp]             		
	                			if k == 'HLT': 
	                				HLT_dict [track.name] = [track.eta, track.phi, track.z0, track.pT, track.d0,track.event,track.hp]             		
	                			if k == 'Offline': 
	                				Offline_dict [track.name] = [track.eta, track.phi, track.z0, track.pT, track.d0,track.event,track.hp]             		
	                			
#for pair in HLT_dict.items():
#	print('HLT',pair) 
#for pair in LRT_dict.items():
 #      print('LRT',pair)
#for pair in Offline_dict.items():
#        print(pair)



np.save('LRT_dict_test.npy',LRT_dict) 
np.save('HLT_dict_test.npy',HLT_dict) 
np.save('Offline_dict_test.npy',Offline_dict) 






####### splitting offline and HLT
start = ['Truth']
ends = ['Offline']

Offline_dict = {}
HLT_dict = {} 
LRT_dict = {}
Truth_dict = {}

for k,l in zip(start, ends): 
	####### making tracks  
	is_track = False 
	copy = False 
	k_dict = {} 
	
	import csv 
	
	with open('test_file1', newline='') as csvfile:
		new_reader = csv.reader(csvfile, delimiter='\t')
		for row in new_reader:
			for i in range(1,len(row)): # seperate offline, HLT, LRT 
	              		fullstring = row[i]
	              		substring = "event" 
	              		if substring in fullstring: 
	               			event_no = row[i]
	              		fullstring = row[i]
	              		substring = k
	              		substring2 = l 
	              		substring3 = 'Truth'
	              		if k == 'LRT': 
	              			if substring in fullstring and substring2 in fullstring: 
	                			copy = True 
	              			if substring2 in fullstring and substring not in fullstring:
	                			copy = False 
	              			if substring3 in fullstring:
	              				copy = False 
	              		
	              				
	              		if k == 'Truth': 
	              			if substring in fullstring: 
	                			copy = True 
	              			if substring2 in fullstring:
	                			copy = False
	                			
	              		else: 
	              			if substring in fullstring: 
	                			copy = True 
	              			if substring2 in fullstring:
	                			copy = False
	              			if substring3 in fullstring:
	                			copy = False     			
	   
                            
			if copy == True:         	
		
	              		for i in range(1,len(row)): # seperate chain line and tracks 
	                		fullstring = row[i]
	                		substring = "Chain" 
	                		if substring in fullstring: 
	                			chain_name = row   
	                			is_track = False 
	                		else: 
	                			is_track = True   
	              		if is_track == True: 
	                		track = Track() # make track and fill it 
	                		
	                		if k == 'Truth': 
	                			if len(row)>9:    
	                			#print(k,len(row)) 
	                				track.event = float(event_no.replace("event:",""))
	                				fullstring = row[4]
	                				substring = "eta" 
	                				if substring in fullstring:
	                					track.eta = float(row[4].replace("eta=",""))
	                				fullstring = row[5]
	                				substring = "phi"
	                				if substring in fullstring:
	                					track.phi = float(row[5].replace("phi=",""))
	                				fullstring = row[6]
	                				substring = "z0" 
	                				if substring in fullstring:
	                					track.z0 = float(row[6].replace("z0=",""))
	                				fullstring = row[7]
	                				substring = "pT" 
	                				if substring in fullstring:
	                					track.pT = float(row[7].replace("pT=","").replace("GeV",""))
	                				fullstring = row[8]
	                				substring = "d0" 
	                				if substring in fullstring:
	                					track.d0 = float(row[8].replace("d0=",""))
	                				fullstring = row[9]
	                				substring = "hp" 
	                				if substring in fullstring:
	                					track.hp = row[9].replace("hp=","")
	                				fullstring = row[13]
	                				substring = "id" 
	                				if substring in fullstring:
	                					ID = row[13]
	                				track.name = chain_name[1] + ' ' + ID + event_no
	                			####### add track to directory 
	                			
	                				if k == 'Truth': 
	                					Truth_dict [track.name] = [track.eta, track.phi, track.z0, track.pT, track.d0,track.event,track.hp]             		
	                			
		
		####### print dictionary  
	
#for pair in Truth_dict.items(): 
#	print(pair) 
	
np.save('Truth_dict_test.npy',Truth_dict)
#for pair in Truth_dict.items():
#	print(pair)
