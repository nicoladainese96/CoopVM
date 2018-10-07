# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 12:48:20 2018

@author: Utente
"""

def swap_matrix_element (A, P):
    import random as r
    S1 = len(A)
    S2 = len(A[0])
    for i in range(P):
        row1 = r.randint(0, S1-1)
        row2 = r.randint(0, S1-1)
        col1 = r.randint(0, S2-1)
        col2 = r.randint(0, S2-1)
        x = A[row1][col1]
        y = A[row2][col2]
        A[row1][col1] = y
        A[row2][col2] = x
    NODF= NODF_calc(A)
    return(A, NODF)
    
def NODF_calc (A):
    #print('Calcolo NODF della corrispondente matrice random.')
    import statistics as stat
    #import math
    import numpy as np
    #print('conn = ', conn)
    #A = random_matrix(int(S1a),int(S2a),float(conn))
    S1 = len(A)
    S2 = len(A[0])
    #print('S1 + S2 = ', S1+S2)
    #print('S1 = ', S1)
    #print('S2 = ', S2)
    k_A = []
    k_P = []
    
    for i in range (len(A)):
        x = 0
        for j in range(len(A[i])):
            x = x + A[i][j]
        k_A.append(x)
    
    for j in range(len(A[0])):
        x = 0
        for i in range(len(A)):
            x = x + A[i][j]
        k_P.append(x)
    
    #print('k_A = ', k_A)
    #print('k_P = ', k_P)
    sigma_deg_A = stat.stdev(k_A)
    sigma_deg_P = stat.stdev(k_P)
    
    
    O_A = [ [] for x in range(S1)]
    O_P = [ [] for x in range(S2)]
    
    for i in range(S1):
        for j in range(S1):
            x = 0
            for k in range(S2):
                x = x + A[i][k]*A[j][k]
            O_A[i].append(x)
    
    for i in range(S2):
        for j in range(S2):
            x = 0
            for k in range(S1):
                x = x + A[k][i]*A[k][j]
            O_P[i].append(x)
    
    T_A = [ [] for x in range(S1)]
    T_P = [ [] for x in range(S2)]
    
    for i in range(S1):
        for j in range(S1):
            if k_A[i] == k_A[j]:
                T_A[i].append(0)
            elif O_A[i][j] == 0:
                T_A[i].append(0)
            else:
                m = min( [k_A[i], k_A[j] ])
                if m == 0:
                    print('Attenzione, min( [k_A[{}], k_A[{}] ]) = 0 '.format(i,j))
                    print('k_A[{}] = {}'.format(i, k_A[i]))
                    print('k_A[{}] = {}'.format(j, k_A[j]))
                    print('O_A[{}][{}] = {}'.format(i,j,O_A[i][j]))
                    m = 0.001
                x = O_A[i][j]/m
                T_A[i].append(x)
    
    for i in range(S2):
        for j in range(S2):
            if k_P[i] == k_P[j]:
                T_P[i].append(0)
            elif O_P[i][j] == 0:
                T_P[i].append(0)
            else:
                m = min( [k_P[i], k_P[j] ])
                if m == 0:
                    print('Attenzione, min( [k_P[{}], k_P[{}] ]) = 0 '.format(i,j))
                    print('k_P[{}] = {}'.format(i, k_P[i]))
                    print('k_P[{}] = {}'.format(j, k_P[j]))
                    print('O_P[{}][{}] = {}'.format(i,j,O_P[i][j]))
                    m = 0.001
                x = O_P[i][j]/m
                T_P[i].append(x)
    
    num_A = 0
    for i in range(S1):
        for j in range(i,S1):
            num_A = num_A + T_A[i][j]
            if np.isnan(num_A):
                print('T_A[i][j] = ', T_A[i][j])
                
    
    num_P = 0
    for i in range(S2):
        for j in range(i,S2):
            num_P = num_P + T_P[i][j]
            if np.isnan(num_P):
                print('T_P[i][j] = ', T_P[i][j])
    den_A = S1*(S1-1)/2
    den_P = S2*(S2-1)/2
    NODF = round((num_A + num_P)/(den_A + den_P),3) 
    #sigma = math.sqrt( pow(sigma_deg_A/S2,2) + pow(sigma_deg_P/S1,2))
    return (NODF) 
