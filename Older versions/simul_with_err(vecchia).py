# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 17:11:47 2018

@author: Utente
"""

def simul_with_err(N1=100, N2=100, p = 0.33, t=10000):
    from one_simulation import one_simulation
    from my_print import print_tuple3
    from my_print import print_gnuplot2a, print_gnuplot3
    from copy import deepcopy
    import math
    import time
    import statistics
    
    start = time.time()
    S1 = int(math.sqrt(N1))
    S2 = int(math.sqrt(N2))
    print("S1 = {}".format(S1))
    print("S2 = {}".format(S2), '\n')
    if p != 0.33:
        name = repr(N1)+'-'+repr(N2)+'-'+'p'
    else:
        name = repr(N1)+'-'+repr(N2)
    eps = 0
    eps_S = []
    for i in range(0,11):
        S_list = ([], [])
        P2j_1 = []
        P2j_2 = []
        Pn = ([],[])
        P_mean = ([],[])
        P_dev = ([],[])
        for j in range(0,10):
            print("Simulazione numero {} con eps = {}".format(j+1,eps))
            (S_mean1, S_mean2, P2_1, P2_2) = one_simulation(N1, N2, S1, S2, eps, p, t, name, j+1)
            #S_mean_j = (S_mean1, S_mean2)
            Pj = (P2_1, P2_2)
            
            if len(P2j_1) == 0:
                #print('Pj = ', Pj)
                #print('Pj[0] = ', Pj[0])
                #P2j[0] = deepcopy(Pj[0])
                P2j_1 = Pj[0][:]
            elif len(P2j_1) < len(Pj[0]) and len(P2j_1) > 0 :
                for w in range(0, len(P2j_1)):
                    P2j_1[w][1].append(Pj[0][w][1][0])
                P2j_1 = P2j_1 + Pj[0][len(P2j_1):]
            else:
                for w in range(0, len(Pj[0])):
                    P2j_1[w][1].append(Pj[0][w][1][0])
                    
            if len(P2j_2) == 0:
                P2j_2= deepcopy(Pj[1])
            elif len(P2j_2) < len(Pj[1]) and len(P2j_2) > 0 :
                for w in range(0, len(P2j_2)):
                    P2j_2[w][1].append(Pj[1][w][1][0])
                P2j_2 = P2j_2 + Pj[1][len(P2j_2):]
            else:
                for w in range(0, len(Pj[1])):
                    P2j_2[w][1].append(Pj[1][w][1][0])
   
            S_list[0].append(S_mean1)
            S_list[1].append(S_mean2)

        
        for k in range(0, len(P2j_1)):
            if len(P2j_1[k][1]) > 1:  
                P_mean[0].append(statistics.mean(P2j_1[k][1]))
                P_dev[0].append(statistics.stdev(P2j_1[k][1]))
                Pn[0].append((k+1,P_mean[0][k], P_dev[0][k]))
            else:
                P_mean[0].append(P2j_1[k][1][0])
                P_dev[0].append(0.0001)
                Pn[0].append((k+1,P_mean[0][k], P_dev[0][k]))
                
        for k in range(0, len(P2j_2)):
            if len(P2j_2[k][1]) > 1:  
                P_mean[1].append(statistics.mean(P2j_2[k][1]))
                P_dev[1].append(statistics.stdev(P2j_2[k][1]))
                Pn[1].append((k+1,P_mean[1][k], P_dev[1][k]))
            else:
                P_mean[1].append(P2j_2[k][1][0])
                P_dev[1].append(0.0001)
                Pn[1].append((k+1,P_mean[1][k], P_dev[1][k]))
        
        #attenzione a questa stampa! tra l'altro la condizione dell'if non ha molto senso
        if i == 1:
            print(repr(Pn))
        #tutto da rifare
        #print_tuple3(Pn, 'Pn_'+name+'-'+repr(nu), name, d=3)
        #print_gnuplot3(name+'-'+repr(nu), name, nu)
        #print('S_list = ', S_list, '\n')
        S_mean_1 = statistics.mean(S_list[0])
        S_dev_1 = statistics.stdev(S_list[0])
        if S_dev_1 == 0:
            S_dev_1 = 0.001
            
        S_mean_2 = statistics.mean(S_list[1])
        S_dev_2 = statistics.stdev(S_list[1])
        if S_dev_2 == 0:
            S_dev_2 = 0.001
        
        eps_S.append((eps, S_mean_1, S_dev_1, S_mean_2, S_dev_2 ))
        eps = round(eps + 1/N1,4)
    
    #tutto da rifare
    #print_tuple3(eps_S, 'eps_S', name, d=3)
    #print_gnuplot2a('gnu', name)
    finish = time.time()
    t_tot = round((finish-start)/60,2)
    print("Tempo totale impiegato = {}".format(t_tot), 'min')
