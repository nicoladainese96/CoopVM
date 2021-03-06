# -*- coding: utf-8 -*-
"""
@author: nicola.dainese96@gmail.com
"""

def R_one_simulation(N1 = 50, N2 = 50, S1 = 10, S2 = 10, eps = 0.05, 
                     p = 0.33, t = 1000, dir_name = '50-50', rip = 1, g=1, flag = False, re = 1):
    from one_step_bi import one_step
    from random import randint
    from copy import deepcopy
    import time
    start_time = time.time()
    name = repr(eps)+'-'+repr(p) +'-'+repr(rip)+'-'+repr(re)
    
    from bipartite_graph_matrix import adjacency_matrix_rnd2
    A = adjacency_matrix_rnd2(S1, S2, p, dir_name, re, g, flag )
    tau_max1 = int(t/N1)
    
   
    v1 = [ randint(0, S1-1) for x in range (0,N1)]
    n1 = []
    Smax1 = max(v1)
    for i in range (0,Smax1+1):
        c1 = v1.count(i)
        n1.append(c1)
        
    v2 = [ randint(0, S2-1) for x in range (0,N2)]
    n2 = []
    Smax2 = max(v2)
    for i in range (0,Smax2+1):
        c2 = v2.count(i)
        n2.append(c2)

    import my_output as O
    
    for i in range (1,tau_max1):
        #qui il programma è un po' imparziale, perchè tratta la specie 1 come standard
        for k in range(0,N1):
            (v1, v2, n1, n2) = one_step(N1, N2, v1, v2, n1, n2, A, eps)
            #(v1, v2, n1, n2) = one_step(N1, N2, v1, v2, n1, n2, A, eps, rip, True, dir_name)
        n_1 = deepcopy(n1)
        S1 = len(n_1) - n_1.count(0)
        O.print_list_csv(S1, 'R_S1_'+name, dir_name, d=1)
        O.print_list_csv(n_1, 'R_n1_'+name, dir_name, d = len(n_1))
        n_2 = deepcopy(n2)
        S2 = len(n_2) - n_2.count(0)
        O.print_list_csv(S2, 'R_S2_'+name, dir_name, d=1)
        O.print_list_csv(n_2, 'R_n2_'+name, dir_name, d = len(n_2))
        
      
    simulation_t = round((time.time() - start_time)/60,4)
    print("Tempo simulazione: {}".format(simulation_t), 'min. \n')

def N_one_simulation(N1 = 50, N2 = 50, S1 = 10, S2 = 10, eps = 0.05, p = 0.33, 
                     t = 1000, dir_name = '50-50', rip = 1, g=1, flag = False, re = 1, option = 0):
    from one_step_bi import one_step
    from random import randint
    from copy import deepcopy
    import time
    start_time = time.time()
    name = repr(eps)+'-'+repr(p) +'-'+repr(rip)+'-'+repr(re)
    
    from bipartite_graph_matrix import adjacency_matrix_nested, adjacency_matrix_nested2
    if option == 0: #asymmetric nested / first type
        A = adjacency_matrix_nested(S1, S2, p , dir_name, re, g, flag)
    else: #balanced nested / second type
        A = adjacency_matrix_nested2(S1, S2, p , dir_name, re, g, flag)
    tau_max1 = int(t/N1)
   
    v1 = [ randint(0, S1-1) for x in range (0,N1)]
    n1 = []
    Smax1 = max(v1)
    for i in range (0,Smax1+1):
        c1 = v1.count(i)
        n1.append(c1)
   
    v2 = [ randint(0, S2-1) for x in range (0,N2)]
    n2 = []
    Smax2 = max(v2)
    for i in range (0,Smax2+1):
        c2 = v2.count(i)
        n2.append(c2)
    
    
    import my_output as O

    for i in range (1,tau_max1):
        #qui il programma è un po' imparziale, perchè tratta la specie 1 come standard
        for k in range(0,N1):
            (v1, v2, n1, n2) = one_step(N1, N2, v1, v2, n1, n2, A, eps)
            #(v1, v2, n1, n2) = one_step(N1, N2, v1, v2, n1, n2, A, eps, rip, True, dir_name)
        n_1 = deepcopy(n1)
        S1 = len(n_1) - n_1.count(0)
        O.print_list_csv(S1, 'N_S1_'+name, dir_name, d=1)
        O.print_list_csv(n_1, 'N_n1_'+name, dir_name, d = len(n_1))
        n_2 = deepcopy(n2)
        S2 = len(n_2) - n_2.count(0)
        O.print_list_csv(S2, 'N_S2_'+name, dir_name, d=1)
        O.print_list_csv(n_2, 'N_n2_'+name, dir_name, d = len(n_2))


        
         
    simulation_t = round((time.time() - start_time)/60,4)
    print("Tempo simulazione: {}".format(simulation_t), 'min. \n')

def one_simulation(A, N1 = 50, N2 = 50, S1 = 10, S2 = 10, eps = 0.05, p = 0.33, 
                     t = 1000, NODF = 1, dir_name = '50-50', rip = 1, g=1, flag = False, re = 1):
    from one_step_bi import one_step
    from random import randint
    from copy import deepcopy
    import time
    from grad_nestedness import NODF_calc
    start_time = time.time()
    
    name = repr(NODF)+'-'+repr(eps)+'-'+repr(p)+'-'+repr(rip)+'-'+repr(re)
    print('name simulation = ', name)
    NODF = NODF_calc(A)
    print('NODF = ', NODF)
    tau_max1 = int(t/N1)
    print('tau = ', tau_max1)
    v1 = [ randint(0, S1-1) for x in range (0,N1)]
    n1 = []
    Smax1 = max(v1)
    for i in range (0,Smax1+1):
        c1 = v1.count(i)
        n1.append(c1)
   
    v2 = [ randint(0, S2-1) for x in range (0,N2)]
    n2 = []
    Smax2 = max(v2)
    for i in range (0,Smax2+1):
        c2 = v2.count(i)
        n2.append(c2)
    
    
    import my_output as O

    for i in range (1,tau_max1):
        #qui il programma è un po' imparziale, perchè tratta la specie 1 come standard
        for k in range(0,N1):
            (v1, v2, n1, n2) = one_step(N1, N2, v1, v2, n1, n2, A, eps)
            #(v1, v2, n1, n2) = one_step(N1, N2, v1, v2, n1, n2, A, eps, rip, True, dir_name)
        n_1 = deepcopy(n1)
        S1 = len(n_1) - n_1.count(0)
        O.print_list_csv(S1, 'S1_'+name, dir_name, d=1)
       # O.print_list_csv(n_1, 'n1_'+name, dir_name, d = len(n_1))
        n_2 = deepcopy(n2)
        S2 = len(n_2) - n_2.count(0)
        O.print_list_csv(S2, 'S2_'+name, dir_name, d=1)
        #O.print_list_csv(n_2, 'n2_'+name, dir_name, d = len(n_2))


        
         
    simulation_t = round((time.time() - start_time)/60,2)
    print("Tempo simulazione: {}".format(simulation_t), 'min. \n')

