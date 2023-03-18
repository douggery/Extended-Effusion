import numpy as np
import math
import matplotlib.pyplot as plt

#This script is built to understand molecular flux 
#in both the near field and in the far field where 
#it reproduces the thermal beam equation. The far field 
#is generally achieved when the distamce between the 
#source and detector are separated by a dist>>lengths

dx=0.1
dy=0.1

def find_center(matrix):
	ycenter=int(matrix.shape[0]/2)
	xcenter=int(matrix.shape[1]/2)
	return [ycenter,xcenter]
	
def gen_coords(matrix):
#function takes in an array and outputs scaled coordinates [x,y]
	center=find_center(matrix)
	for i in range(matrix.shape[0]):
		for j in range(matrix.shape[1]):
			matrix[i][j][0]=(center[0]-i)*dx
			matrix[i][j][1]=(j-center[1])*dy


def calc_flux(s,d,d_flux,dist):
	
#the differential element of flux must take into account
#the solid angle emitted; otherwise it will overestimate
#the flux striking a surface at a large distance as compared 
#to the flux striking an identical surface at a short distance

	dQ=1*dx*dy/(dist**2)
	
	tot_flux=0
	for i in range(s.shape[0]):
		for j in range(s.shape[1]):
			for k in range(d.shape[0]):
				for l in range(d.shape[1]):
					df=dQ*dist**2/((s[i][j][1]-d[k][l][1])**2+(s[i][j][0]-d[k][l][0])**2+dist**2)
					d_flux[k][l]+=df				
					tot_flux+=df
	print("The total flux is", tot_flux)
	return tot_flux

def plotter(map):
	fig1, ax1= plt.subplots()
	plt.imshow(map,origin="lower", cmap='gist_heat',interpolation='nearest')
	plt.colorbar()
	plt.show()

def screen():
	#need to detect the line from the source point to 
	#each edge of the detector (which is just the term 
	#for the skimmer)
	return 0

def run_sim(h1,w1,h2,w2,dist):
	source=np.zeros((h1,w1,2))
	detector=np.zeros((h2,w2,2))
	detectorFlux=np.zeros((h2,w2))
	
	gen_coords(source)

	gen_coords(detector)

	calc_flux(source,detector,detectorFlux,dist)
	plotter(detectorFlux)

d=6

run_sim(3,3,500,500,d)
#run_sim(3,3,500,500,d**2)
#run_sim(3,3,500,500,d**3)
#run_sim(3,3,500,500,d**4)

