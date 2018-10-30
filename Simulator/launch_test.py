# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:10:18 2018
Sort of user interface used to execute all kinds of simulation of CVM. 
Directly executable from Python console.
@author: nicola.dainese96@gmail.com
"""
import time
from NODF_swap import NODF_swap #this code is full of trubles - not used in the thesis' version
import one_simul_launcher as launch
#from main import tau_conv #this part can be improved - not all main.py file is required
from t_conv import t_conv
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#This directory at the moment has to be written by the user. 
work_dir = 'C:/Users/Utente/Anaconda3/SpeedTest'
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#Actually more than a working directory it's the folder in which all the data 
#from a simulation are printed.
N = 1000 #number of individuals of each VM
S1 = 34 #number of species of the first group - usually I set S = sqrt(N)
S2 = 34  #number of species of the first group
rip = 10 #number of realization for each value of the parameters - 100 suggested for statistic significance
eps = 0.1 #epsilon - intensity of mutualism
p = 0.35 #probability of an element matrix Mij to be 1 - on average is equal to the connectance C
epsilons = [0.0, 0.033, 0.066, 0.1, 0.2, 0.35, 0.5, 0.65, 0.8, 1.0] #set of values for epsilon
ps = [0.0, 0.033, 0.066, 0.1, 0.2, 0.35, 0.5, 0.65, 0.8, 1.0] #set of values for p (~C)
#ps = [0.35, 0.4]
start = time.time()
#t = tau_conv(N) #it's measured in steps -> change the name of 'tau_conv' function!!
t = t_conv(N, s=3)
end = time.time()
diff = round((end-start)/60,4)
print('Time employed to compute t_conv: {} min \n'.format(diff))
#t = 100000 #(time can be specified also manually)
#Note that the result form tau_conv(N) can vary for the very same N 
#(because basically it depends on absorption time of a single Voter Model 
#without speciation and cooperation)
#so this could cause some troubles in comparing two results of simulations with 
#same input parameters but different t
#
#parameters for NODF_launcher
step = 100 #variables inherited from an older version - don't change it
P = 1 #variables inherited from an older version - don't change it
rip2 = 200 #number of realization for each value of the parameters
C = 0.35 #connectance
eps2 = 0.1 #epsilon - intensity of mutualism 
#
#at this dir_name could be added the time of the simulation, resulting from tau_conv call
dir_name = work_dir+'/NODF/'+repr(C)+'-'+repr(step)+'-'+repr(P)+'-'+repr(rip2)

commands = [1] #select [0,1,2,3,4] to execute all statements
for x in commands:
    if x == 0:
        #vary the connectance with fixed epsilon
        #the last entry (0 or 1) specifies which kind of synthetic nested to use
        #I suggest the 1 option because it's more balanced
        launch.p_launcher(N, rip, eps, ps, t, work_dir, 0)
        #this option feature should be improved in a more clear way
    elif x == 1:
        #vary epsilon (mutualism intensity) with fixed connectance
        launch.e_launcher(N, rip, epsilons, p, t, work_dir)
    elif x == 2:
        print('Eseguo NODF_launcher.')
        #l'ultima variabile è 'option', che per 0 fa nested2 (maggiore NODF iniziale), 
        #altrimenti nested e basta
        launch.NODF_launcher(N, S1, S2, C, eps2, step, P, rip2, t, work_dir, 0)
        #launch.NODF_launcher(N, S1, S2, C, eps2, step, P, rip2, t, work_dir, 1)
        #eps2 = 0.5
        #launch.NODF_launcher(N, S1, S2, C, eps2, step, P, rip2, t, work_dir)
        #C = 0.2
        #launch.NODF_launcher(N, S1, S2, C, eps2, step, P, rip2, t, work_dir)
    elif x == 3:
        print('Eseguo precision_simul.')
        #this parameters should be local variables
        #so they don't interfere with the statements above
        C = 0.35
        eps = 0.1
        rip = 50
        #run for comparing (for fixed espilon and C) random and balanced nested cases 
        #it could be extended to asymmetric nested case too
        launch.precision_simul(N, S1, S2, C, eps, rip, t, work_dir)
    elif x == 4:
        #to be revised
        print('Eseguo NODF_swap.')
        NODF_swap(S1, S2, 0.35, step, 2, dir_name)
    else:
        continue
    
import winsound #hope this library works for all operating systems and not just for windows
#anyway it's just an alert
duration = 500  # millisecond
freq = 600  # Hz
winsound.Beep(freq, duration)
print('launching_test eseguito.')
    
