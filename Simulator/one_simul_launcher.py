# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 08:53:37 2018

@author: nicola.dainese96@gmail.com
"""
def p_launcher (N, rip, eps, ps, t, work_dir, option):
    import math
    import time
    from one_simulation import R_one_simulation, N_one_simulation
    import my_output as O
    start = time.time()
    N1 = N
    N2 = N
    S1 = int(math.sqrt(N1))
    S2 = int(math.sqrt(N2))
    tau_max1 = int(t/N1)
    parent_dir = work_dir+'/'+repr(N)+'-'+repr(rip)+'-'+repr(tau_max1)+'/p'
    for p in ps:
        dir_name = parent_dir+'/'+repr(eps)+'-'+repr(p)
        for i in range(rip):
            print('Eseguo simulazione random numero {} su {} con (eps, p) = ( {}, {})'.format(i+1,rip, eps, p))
            R_one_simulation(N1, N2, S1, S2, eps, p, t, dir_name, rip, re =i)
        O.R_print_info_csv(eps, p, rip, dir_name, parent_dir)
        for i in range(rip):
            print('Eseguo simulazione nested numero {} su {} con (eps, p) = ( {}, {})'.format(i+1,rip, eps, p))
            N_one_simulation(N1, N2, S1, S2, eps, p, t, dir_name, rip, re = i, option = option)
        O.N_print_info_csv(eps, p, rip, dir_name, parent_dir)
    O.info_p(N, rip, eps, ps, t, work_dir, parent_dir)
    end = time.time()
    elapsed = round((end-start)/60,4)
    print('p_launcher eseguito in {} min \n'.format(elapsed))
    
def e_launcher (N, rip, epsilons, p, t, work_dir):
    import math
    import time
    from one_simulation import R_one_simulation, N_one_simulation
    import my_output as O
    start = time.time()
    N1 = N
    N2 = N
    S1 = int(math.sqrt(N1))
    S2 = int(math.sqrt(N2))
    tau_max1 = int(t/N1)
    parent_dir = work_dir+'/'+repr(N)+'-'+repr(rip)+'-'+repr(tau_max1)+'/e'
    for eps in epsilons:
        dir_name = parent_dir+'/'+repr(eps)+'-'+repr(p)
        for i in range(rip):
            print('Eseguo simulazione random numero {} su {} con (eps, p) = ( {}, {})'.format(i+1,rip, eps, p))
            R_one_simulation(N1, N2, S1, S2, eps, p, t, dir_name, rip, re =i)
        O.R_print_info_csv(eps, p, rip, dir_name, parent_dir)
        for i in range(rip):
            print('Eseguo simulazione nested numero {} su {} con (eps, p) = ( {}, {})'.format(i+1,rip, eps, p))
            N_one_simulation(N1, N2, S1, S2, eps, p, t, dir_name, rip, re = i)
        O.N_print_info_csv(eps, p, rip, dir_name, parent_dir)
    O.info_e(N, rip, epsilons, p, t, work_dir, parent_dir)
    end = time.time()
    elapsed = round((end-start)/60,2)
    print('c_launcher eseguito in {} min \n'.format(elapsed))
    
def NODF_launcher(N, S1, S2, C, eps, step, P, rip, t, work_dir, option):
    import time
    from one_simulation import one_simulation
    from bipartite_graph_matrix import adjacency_matrix_nested2, adjacency_matrix_nested
    import my_output as O
    #from NODF_swap import swap_matrix_element, NODF_swap2
    from grad_nestedness import swap_matrix_element, NODF_calc
    import os
    N1 = N
    N2 = N
    start = time.time()
    if option == 0:
        parent_dir = work_dir+'/NODF/op0/'
    else:
        parent_dir = work_dir+'/NODF/op1/'
    dir_name = parent_dir+repr(C)+'-'+repr(eps)+'-'+repr(rip)
    
    matrix_dir = dir_name+'/matrix'
    if option == 0:
        print('Eseguo matrice nested nuova.')
        A = adjacency_matrix_nested2(S1, S2, C, dir_name, 0)
    else:
        print('Eseguo matrice nested vecchia.')
        A = adjacency_matrix_nested(S1, S2, C, dir_name, 0)
        
    NODF = NODF_calc(A)
    A0 = A
    NODFs = []
    NODFs.append(NODF)
    #(As, NODFs) = NODF_swap2(S1, S2, C, step, P, dir_name, option)
    #from NODF_swap import NODF_swap3
    #(As, NODFs) = NODF_swap3(S1, S2, C, step, P, dir_name)
    file_path2 = "C:/Users/Utente/Anaconda3/UserScripts/Programmi cooperazione/"
    directory2 = os.path.dirname(file_path2)
    os.chdir(directory2)
    T = True
    for i in range(10):
        if i == 0:
            O.print_matrix2(A0, S1, S2, C, NODF, 0, matrix_dir)
            for j in range(rip):
                print('Eseguo simulazione numero {} su {} con NODF = {}'.format(j+1,rip, NODF))
                one_simulation(A0, N1, N2, S1, S2, eps, C, t, NODF, dir_name, rip, re = j)
            O.NODF_print_info_csv(NODFs[i], eps, C, rip, dir_name, parent_dir)
       
        else:
            (A, NODF) = swap_matrix_element(A0,P*i)
            tentativo = 1
            while NODF > NODFs[-1] - 0.04 :
                (A, NODF) = swap_matrix_element(A0,P*i)
                tentativo = tentativo + 1
                if tentativo > 10000:
                    T = False
                    break
            if T == True:
                print('Matrice selezionata al tentativo numero ', tentativo)
                NODFs.append(NODF)
                O.print_matrix2(A, S1, S2, C, NODF, i, matrix_dir)
                for j in range(rip):
                    print('Eseguo simulazione numero {} su {} con NODF = {}'.format(j+1,rip, NODF))
                    one_simulation(A, N1, N2, S1, S2, eps, C, t, NODF, dir_name, rip, re = j)
                O.NODF_print_info_csv(NODFs[i], eps, C, rip, dir_name, parent_dir)
    O.info_NODF(N, rip, NODFs, eps, C, t, work_dir, parent_dir)
    
    end = time.time()
    elapsed = round((end-start)/60,2)
    print('NODF_launcher eseguito in {} min \n'.format(elapsed))
    
def precision_simul(N, S1, S2, C, eps, rip, t, work_dir):
    import time
    from one_simulation import one_simulation
    import my_output as O
    from grad_nestedness import NODF_calc
    N1 = N
    N2 = N
    start = time.time()
    parent_dir = work_dir + '/precision/'
    dir_name1 = parent_dir+'/nuova/'
    dir_name2 = parent_dir+'/vecchia/'
    
    from bipartite_graph_matrix import adjacency_matrix_nested2, adjacency_matrix_rnd2
    
    print('Eseguo matrice nested nuova.')
    A1 = adjacency_matrix_nested2(S1, S2, C, dir_name1, 1)
    NODF1 = NODF_calc(A1)
    
    for i in range(rip):
        one_simulation(A1, N1, N2, S1, S2, eps, C, t, NODF1, dir_name1, rip, re = i)
    O.NODF_print_info_csv(NODF1, eps, C, rip, dir_name1, parent_dir)
    O.info_precision(N, rip, [NODF1], eps, C, t, work_dir, parent_dir)
    
    print('Eseguo matrice random.')
    A2 = adjacency_matrix_rnd2(S1, S2, C, dir_name2, 1)
    NODF2 = NODF_calc(A2)
   
    for i in range(rip):
        one_simulation(A2, N1, N2, S1, S2, eps, C, t, NODF2, dir_name2, rip, re = i)
    O.NODF_print_info_csv(NODF2, eps, C, rip, dir_name2, parent_dir)
    O.info_precision(N, rip, [NODF2], eps, C, t, work_dir, parent_dir)
    
    end = time.time()
    elapsed = round((end-start)/60,2)
    print('NODF_launcher eseguito in {} min \n'.format(elapsed))
    