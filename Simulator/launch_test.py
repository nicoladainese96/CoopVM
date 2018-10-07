# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:10:18 2018
Sort of user interface used to execute all kinds of simulation of cvm.
@author: nicola.dainese96@gmail.com
"""
from NODF_swap import NODF_swap
import one_simul_launcher as launch
from main import tau_conv

#This directory at the moment has to be written by the user. 
work_dir = 'C:/Users/Utente/Anaconda3/Cooperazione'
#Actually more than a working directory it's the folder in which all the data from
#a simulation are printed.

N = 100
S1 = 10
S2 = 10
C = 0.35
step = 100
P = 1 #uno su C
rip2 = 200
eps2 = 0.1
dir_name = work_dir+'/NODF/'+repr(C)+'-'+repr(step)+'-'+repr(P)+'-'+repr(rip2)
#
rip = 2
eps = 0.1
p = 0.35
epsilons = [0.0, 0.033, 0.066, 0.1, 0.2, 0.35, 0.5, 0.65, 0.8, 1.0]
ps = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55]

#t = tau_conv(N)
#t = 150001
t = 7500
commands = [0]
for x in commands:
    if x == 0:
        
        
        launch.p_launcher(N, rip, eps, ps, t, work_dir, 0)
    elif x == 1:
        
       
        launch.e_launcher(N, rip, epsilons, p, t, work_dir)
    elif x == 2:
        print('Eseguo NODF_launcher.')
        
        #l'ultima variabile è 'option', che per 0 fa nested2 (maggiore NODF iniziale), altrimenti nested e basta
        launch.NODF_launcher(N, S1, S2, C, eps2, step, P, rip2, t, work_dir, 0)
        #launch.NODF_launcher(N, S1, S2, C, eps2, step, P, rip2, t, work_dir, 1)
        #eps2 = 0.5
        #launch.NODF_launcher(N, S1, S2, C, eps2, step, P, rip2, t, work_dir)
        #C = 0.2
        #launch.NODF_launcher(N, S1, S2, C, eps2, step, P, rip2, t, work_dir)
    elif x == 3:
        print('Eseguo precision_simul.')
        
        C = 0.35
        eps = 0.1
        rip = 50
        launch.precision_simul(N, S1, S2, C, eps, rip, t, work_dir)
    elif x == 4:
        print('Eseguo NODF_swap.')
        NODF_swap(S1, S2, 0.35, step, 2, dir_name)
    else:
        continue
    
import winsound
duration = 500  # millisecond
freq = 600  # Hz
winsound.Beep(freq, duration)
print('launching_test eseguito.')
    
