import csv
import subprocess

counter =0
with open("ligand_list.csv","r",newline='') as f:
	reader=csv.reader(f, delimiter='\t')
	for row in reader:  #we find which column we have our SMILES in
		
		for col in row: #iterating through the rows
			counter+=1
			
			if "SMILE" in col: 
				counter=counter-1
				break
		break
	
	
	counter2=0	#will count how many molecules get converted to pdb
	print("Running")
	for row in reader:  
		
		subprocess.call(['bash', 'pipeline.sh',row[0], row[counter]],shell=False)
		counter2+=1


	print(counter2,"Molecules converted to PDB")
	f.close()


