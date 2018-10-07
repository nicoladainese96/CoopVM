# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 17:00:45 2018

@author: nicola.dainese96@gmail.com
"""


#from one_simulation import one_simulation
#(S_mean1, S_mean2, P2_1, P2_2) = one_simulation()
#from simul_with_err import simul_with_err
#simul_with_err(N1=50, N2=50, p = 0.33, t=10000)

from main import main_simulation
from main2 import main2
#from one_simulation import one_simulation
from bipartite_graph_matrix import adjacency_matrix_rnd, adjacency_matrix_nested
import time 
import math
from init_simulation import init_simulation2
start = time.time()
parent_dir = 'C:/Users/Utente/Anaconda3/Cooperazione'
x = 0
if x == 0:
    #for n in range(5,11):
    #    N1 = n*n
    #    N2 = n*n
    #    print(N1, N2)
    N1, N2 = 36,36
    #per simulazioni leggere
    #rip = int(math.sqrt(N1))
    #per simulazioni più pesanti usare 
    rip = 2
    main_simulation(N1, N2, rip, p = 0.35, parent_dir = parent_dir)
    #N1, N2 = 100, 100
    #rip = 10
    #main_simulation(N1, N2, rip, p = 0.40)
elif x == 1:
    p = 0.25
    for k in range(0,5):
        main_simulation(N1 = 100, N2 = 100, p = p, parent_dir = parent_dir)
        p = round(p + 0.05,2)
        #print(format(p,'.2f'))
    p = 0.25
    for k in range(5):
        main_simulation(N1 = 200, N2 = 200, p = p, parent_dir = parent_dir)
        p = round(p + 0.05,2)
elif x == 2:
    A = adjacency_matrix_rnd(15,15)
    print(A)
elif x == 3:
    Cs = [0.35]
    for p in Cs:
        main2(N1 = 100, N2 = 100, p = p, rip = 3)
else:
    #A2 = adjacency_matrix_nested()
    #A1 = A = adjacency_matrix_rnd()
    init_simulation2(100, 2, 'Dominanza', '100-2')
finish = time.time()
t_tot = round((finish - start)/60,2)
print('Tempo totale impiegato per il tester = ', t_tot)

import winsound
duration = 500  # millisecond
freq = 600  # Hz
winsound.Beep(freq, duration)

print('Tester eseguito con successo.')