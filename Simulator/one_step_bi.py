# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 09:49:02 2018

@author: nicola.dainese96@gmail.com
"""

def one_step(N1, N2, v1, v2, n1, n2, A, eps, rip = 1, flag = False, dir_name = ''):
    
    (v1,n1) = one_step_A(N1, N2, v1, n1, n2, A, eps, rip = rip, flag = flag, dir_name = dir_name)
    (v2,n2) = one_step_B(N1, N2, v2, n1, n2, A, eps, rip = rip, flag = flag, dir_name = dir_name)
    return (v1, v2, n1, n2)
    
def one_step_A(N1, N2, v1, n1, n2, A, eps, rip, flag, dir_name):
    """ """
    import numpy as np
    from random import random
    from random import sample #da cambiare
    
    Nr = N1 - 1
    q = sample(range(0,N1),1)[0] #posizione nel vettore
    Si = v1[q] #valore di quell'elemento
    n1[Si] = n1[Si] - 1 #aggiorno il conto individui
    Smax2 = len(n1) #perché l'ho chiamato così??
    
    P = np.zeros(Smax2)
    dT = np.zeros(Smax2)
    H_theta = np.ones(Smax2)
    
    for i in range(Smax2):
        if n1[i] == 0:
            H_theta[i] = 0
      
    #M = A.dot(n2)
    dT = eps/N2 *  A.dot(n2)  * H_theta    #vectorial notation with elementwise numpy

    P = n1/Nr + dT
    Ptot = P.sum()
    #RINORMALIZZARE LE PROBABILITÀ
    P = P/Ptot
    if round(P.sum(),2) != 1.0:
        print('Problema Ptot = {} \n'.format(round(P.sum(),2)))
    Ptot_n = 0
    Pc = np.zeros(Smax2) #prob cumulata
   
    for i in range(0, len(P)):
        Ptot_n = Ptot_n + P[i]
        Pc[i] = Ptot_n
    if round(Ptot_n,4) != 1.0:
        print('Ptot norm = ', round(Ptot_n,4))    
        
    C = random()
    for i in range(0, len(P)):
        if Pc[i] < C:
            continue
        elif Pc[i] > C:
            v1[q] = i
            n1[i] = n1[i] + 1
            break

    return(v1,n1)        

def one_step_B(N1, N2, v2, n1, n2, A, eps, rip, flag, dir_name):
    """ """
    
    from random import random
    from random import sample
    import numpy as np
    Nr = N2 - 1
    q = sample(range(0,N2),1)[0] #posizione nel vettore
    Si = v2[q] #valore di quell'elemento
    n2[Si] = n2[Si] - 1 #aggiorno il conto individui
    Smax2 = len(n1) #perché l'ho chiamato così??
    P = np.zeros(Smax2)
    dT = np.zeros(Smax2)
    H_theta = np.ones(Smax2)
    for i in range(Smax2):
        if n2[i] == 0:
            H_theta[i] = 0
    dT = eps/N1 *  A.dot(n1)  * H_theta   
    #M1 = np.array(A.T.dot(n1)).ravel() #vectorial notation with elementwise numpy
    #dT = eps/N1 * H_theta *  M1 #vectorial notation with elementwise numpy
    P = n2/Nr + dT
    Ptot = P.sum()
    #RINORMALIZZARE LE PROBABILITÀ
    P = P/Ptot
    if round(P.sum(),2) != 1.0:
        print('Problema Ptot = {} \n'.format(round(P.sum(),2)))
    Ptot_n = 0
    Pc = np.zeros(Smax2) #prob cumulata
    #rivedere se i cicli range possono essere scritti meglio!!
    for i in range(0, len(P)):
        Ptot_n = Ptot_n + P[i]
        Pc[i] = Ptot_n
    if round(Ptot_n,4) != 1.0:
        print('Ptot norm = ', round(Ptot_n,4))    
        
    C = random()
    for i in range(0, len(P)):
        if Pc[i] < C:
            continue
        elif Pc[i] > C:
            v2[q] = i
            n2[i] = n2[i] + 1
            break

    return(v2,n2)        

def one_step_mono(N, nu, v, n, c_s):
    """ """
    #@@@@@@@@@@@@@@@@@@@@@@@
    #qui ho lasciato il codice di purePython al momento!!
    #@@@@@@@@@@@@@@@@@@@@@@@
    from random import random
    from random import sample
    Nr = N - 1
    q = sample(range(0,N),1)[0] #posizione nel vettore
    Si = v[q] #valore di quell'elemento
    n[Si] = n[Si] - 1 #aggiorno il conto individui
    #if n[Si] == 0:
        #print("Specie {} estinta allo step {}.".format(Si, c_s))
    #creiamo una lista di probabilità
    P = []
    Smax2 = len(n)
    for i in range(0,Smax2): 
        Pb = (1-nu)*n[i]/Nr #prob i-esima nascita
        P.append(Pb)
    
    Ps = nu #probabilità nuova specie
    Ptot = 0
    Pc = [] #prob cumulata
    for i in range(0, len(P)):
        Ptot = Ptot + P[i]
        Pc.append(Ptot)
    Ptot = Ptot + Ps

    C = random()
    for i in range(0, len(P)):
        if Pc[i] < C:
            continue
        elif Pc[i] > C:
            v[q] = i
            n[i] = n[i] + 1
            break
    if Pc[-1] < C:
            (v,n) = speciazione(v,n,q)
    #print("n = ", repr(n))        
    return(v,n)        

def speciazione(v,n,q):
    """ """
    if min(n) == 0:
        for i in range(0, len(n)):
            if n[i] == 0:
                n[i] = 1
                v[q] = i
                break
            else:
                continue
    else:
        S_max = len(n)
        S_nu = S_max
        n.append(1)
        v[q] = S_nu

    return (v,n)

    
            
