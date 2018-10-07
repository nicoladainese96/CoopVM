# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 13:09:06 2018
Swap matrix elements and calculate NODF. Code has a lot of problems, it has to be debugged.
@author: Utente
"""

def NODF_swap (S1, S2, C, step, P, dir_name):
    from grad_nestedness import swap_matrix_element, NODF_calc
    from bipartite_graph_matrix import adjacency_matrix_nested2
    import my_output as O
    NODFs = []
    matrix_dir = dir_name+'/matrix_step'
    A = adjacency_matrix_nested2(S1, S2, C, dir_name, 0)
    NODF = NODF_calc(A)
    
    O.print_matrix2(A, S1, S2, C, NODF, 0, matrix_dir)
    
    
    NODFs.append(NODF)
    for i in range(step):
        (A, NODF) = swap_matrix_element(A,P)
        O.print_matrix2(A, S1, S2, C, NODF, i+1, matrix_dir)
        NODFs.append(NODF)
        
    O.print_NODF_step(NODFs, C, P, dir_name)

#somehow it doesn't work
def NODF_swap2 (S1, S2, C, step, P, dir_name, option):
    #import matplotlib.pyplot as plt
    import numpy as np
    from grad_nestedness import swap_matrix_element, NODF_calc
    from bipartite_graph_matrix import adjacency_matrix_nested2, adjacency_matrix_nested
    import my_output as O
    NODFs = []
    matrix_dir = dir_name+'/matrix'
    if option == 0:
        print('Eseguo matrice nested nuova.')
        A = adjacency_matrix_nested2(S1, S2, C, dir_name, 0)
    else:
        print('Eseguo matrice nested vecchia.')
        A = adjacency_matrix_nested(S1, S2, C, dir_name, 0)
        
    NODF = NODF_calc(A)
    A0 = A
    #print('Astart = ', Astart)
    #NODFstart = NODF
    #print('NODFstart = ', NODFstart)
    O.print_matrix2(A, S1, S2, C, NODF, 0, matrix_dir)
    NODFs.append(round(NODF,3))
    A1, A2, A3, A4, A5, A6, A7, A8 = [],[],[],[],[],[],[],[]
    As = [A0, A1, A2, A3, A4, A5, A6, A7, A8] 
    M = NODF+0.001
    m = 0.25
    selection = np.linspace(m,M,10)
    #print('selection = ', selection)
    for i in range(len(selection)):
        print('selection[-{}] = '.format(i+1), selection[-i-1])
    counts = 1
    tentativo = 1
    m2 = min([ selection[-counts], NODFs[-1] ])
    while counts < len(selection)-1:
        
        (A, NODF) = swap_matrix_element(A0,P)
            
        if NODF < m2 and NODF > selection[-counts-2]:
            
            NODFs.append(round(NODF,3))
            As[counts] = A
            O.print_matrix2(A, S1, S2, C, NODF, counts, matrix_dir)
            counts = counts + 1
            print('Matrice numero {} selezionata al tentativo {} con NODF = {}'.format(counts,tentativo, NODFs[-1]))
            tentativo = 1
            m2 = min([ selection[-counts], NODFs[-1] ])
            if counts < len(selection)-1:
                print('Cerco {} < NODF < {}: \n'.format(round(selection[-counts-2],3) , round(m2,3)) )
          
            
        else:
            print('NODF trovata = ', NODF)
            print('NODF richiesta tra {} e {}'.format(selection[-counts-2], min([selection[-counts],NODFs[-1]]) ))
            tentativo = tentativo + 1
            
        
    #As = [A0, A1, A2, A3, A4, A5, A6, A7, A8, A9] 
    #questo è da cambiare
    O.print_NODF_step2(NODFs, C, P, dir_name)

    print('len(As) = ', len(As))
    print('len(NODFs) = ', len(NODFs))
    for i in range(len(As)):
        print(As[i], '\n')
    return ([A0, A1, A2, A3, A4, A5, A6, A7, A8] , NODFs)

   
    
    
def NODF_swap3 (S1, S2, C, step, P, dir_name):
    import matplotlib.pyplot as plt
    import numpy as np
    from grad_nestedness import swap_matrix_element, NODF_calc
    from bipartite_graph_matrix import adjacency_matrix_nested2, adjacency_matrix_rnd2
    import my_output as O
    NODFs = []
    matrix_dir = dir_name+'/matrix'
    
    print('Eseguo matrice nested nuova.')
    A = adjacency_matrix_nested2(S1, S2, C, dir_name, 0) 
    NODF = NODF_calc(A)
    #print('NODFstart = ', NODFstart)
    O.print_matrix2(A, S1, S2, C, NODF, 0, matrix_dir)
    NODFs.append(round(NODF,3))
    As = []
    As.append(A)
    for i in range(100):
        A = adjacency_matrix_rnd2(S1, S2, C)
        NODF = NODF_calc(A)
        NODFs.append(round(NODF,3))
        As.append(A)
        O.print_matrix2(As[-1], S1, S2, C, NODF, i, matrix_dir)
    return (As, NODFs)
    
    
    
    
    
    