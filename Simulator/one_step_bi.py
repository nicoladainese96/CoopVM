# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 09:49:02 2018

@author: Utente
"""

def one_step(N1, N2, v1, v2, n1, n2, A, eps, rip = 1, flag = False, dir_name = ''):
    
    (v1,n1) = one_step_A(N1, N2, v1, n1, n2, A, eps, rip = rip, flag = flag, dir_name = dir_name)
    (v2,n2) = one_step_B(N1, N2, v2, n1, n2, A, eps, rip = rip, flag = flag, dir_name = dir_name)
    return (v1, v2, n1, n2)
    
def one_step_A(N1, N2, v1, n1, n2, A, eps, rip, flag, dir_name):
    """ """
    
    from random import random
    from random import sample
    import my_print as my
    
    Nr = N1 - 1
    q = sample(range(0,N1),1)[0] #posizione nel vettore
    Si = v1[q] #valore di quell'elemento
    n1[Si] = n1[Si] - 1 #aggiorno il conto individui
    #creiamo una lista di probabilità
    P = []
    Smax2 = len(n1)
    dT = []
    
    for i in range(0,Smax2):
        Ti = 0
        if n1[i] > 0:
            for j in range(0, len(n2)):
                Ti = Ti + eps*A[i][j]*n2[j]/N2
        else:
            Ti = 0
        dT.append(Ti)
    
    for i in range(0,Smax2): 
        Pb = n1[i]/Nr + dT[i]  #prob i-esima nascita
        P.append(Pb)
    
    Ptot = 0
    for i in range(0, len(P)):
        Ptot = Ptot + P[i]
    
    
    #RINORMALIZZARE LE PROBABILITÀ
    for i in range(0, len(P)):
        P[i] = P[i]/Ptot
     
    Ptot_n = 0
    Pc = [] #prob cumulata
    for i in range(0, len(P)):
        Ptot_n = Ptot_n + P[i]
        Pc.append(Ptot_n)
    if round(Ptot_n,4) != 1:
        print('Ptot norm = ', round(Ptot_n,4))    
    
    #fare la stessa cosa anche per one_step_B!!
    if flag == True:
        data = [round(Ptot,2)]
        T_tot = 0
        for i in range(len(dT)):
            T_tot = T_tot + dT[i]
        TsuP = round(T_tot/Ptot,2)
        data.append(TsuP)
        V1 = round(P[0] - P[-1],4)
        data.append(V1)
        V2 = round((dT[0] - dT[-1])/Ptot , 4)    
        data.append(V2)
        my.print_tuple(data, 'A-'+repr(rip), dir_name, d= 4)
        #my.print_tuple(dT, 'dT_A'+repr(rip), dir_name, d= len(dT))
        
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
    import my_print as my
    
    Nr = N2 - 1
    q = sample(range(0,N2),1)[0] #posizione nel vettore
    Si = v2[q] #valore di quell'elemento
    n2[Si] = n2[Si] - 1 #aggiorno il conto individui
    #creiamo una lista di probabilità
    P = []
    dT = []
    
    for i in range(0,len(n2)):
        Ti = 0
        if n2[i] > 0:
            for j in range(0, len(n1)):
                Ti = Ti + eps*A[j][i]*n1[j]/N1
        else:
            Ti = 0
        dT.append(Ti)
    
    for i in range(0,len(n2)): 
        Pb = n2[i]/Nr + dT[i]  #prob i-esima nascita
        P.append(Pb)
    
    Ptot = 0
    for i in range(0, len(P)):
        Ptot = Ptot + P[i]
    #print('Ptot non norm = {}'.format(Ptot))
    
        
    #RINORMALIZZARE LE PROBABILITÀ
    for i in range(0, len(P)):
        P[i] = P[i]/Ptot
     
    Ptot_n = 0
    Pc = [] #prob cumulata
    for i in range(0, len(P)):
        Ptot_n = Ptot_n + P[i]
        Pc.append(Ptot_n)
    #print('Ptot norm = {}'.format(Ptot_n))    
    if round(Ptot_n,4) != 1:
        print('Ptot norm = ', round(Ptot_n,4))
        
    #fare la stessa cosa anche per one_step_B!!
    if flag == True:
        data = [round(Ptot,2)]
        T_tot = 0
        for i in range(len(dT)):
            T_tot = T_tot + dT[i]
        TsuP = round(T_tot/Ptot,2)
        data.append(TsuP)
        V1 = round(P[0] - P[-1],4)
        data.append(V1)
        V2 = round((dT[0] - dT[-1])/Ptot , 4)    
        data.append(V2)
        my.print_tuple(data, 'B-'+repr(rip), dir_name, d=4)
        #my.print_tuple(dT, 'dT_B'+repr(rip), dir_name, d= len(dT))
        
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

    
            
