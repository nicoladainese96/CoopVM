def R_one_simulation(N1 = 50, N2 = 50, S1 = 10, S2 = 10, eps = 0.05, 
                     p = 0.33, t = 1000, dir_name = '50-50', rip = 1, g=1, flag = False):
    from one_step_bi import one_step
    from random import randint
    from copy import deepcopy
    import time
    start_time = time.time()
    name = 'R-'+format(p,'.2f') +'-'+repr(eps)+'-'+repr(rip)
    
    from matrici import adjacency_matrix_rnd
    A = adjacency_matrix_rnd(S1, S2, p, dir_name, rip, g, flag )
    tau_max1 = int(t/N1)
    #tau_max2 =  int(t/N2)
   
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

    from my_print import print_tuple
    
    S_range_1 = 0
    S_range_2 = 0
    for i in range (1,tau_max1):
        #qui il programma è un po' imparziale, perchè tratta la specie 1 come standard
        for k in range(0,N1):
            (v1, v2, n1, n2) = one_step(N1, N2, v1, v2, n1, n2, A, eps)
            #(v1, v2, n1, n2) = one_step(N1, N2, v1, v2, n1, n2, A, eps, rip, True, dir_name)
        n_1 = deepcopy(n1)
        S1 = len(n_1) - n_1.count(0)
        print_tuple([i,S1], 'S1_'+name, dir_name)
        print_tuple(n_1, 'n1_'+name, dir_name, d = len(n_1))
        if S_range_1 < S1:
            S_range_1 = S1
        n_2 = deepcopy(n2)
        S2 = len(n_2) - n_2.count(0)
        print_tuple([i,S2], 'S2_'+name, dir_name)
        print_tuple(n_2, 'n2_'+name, dir_name, d = len(n_2))
        if S_range_2 < S2:
            S_range_2 = S2


    from data_analysis import asymptotic_S_1, Pn, t_start, Pn_cumulative2
    from my_print import tab_reader
    from my_print import tab_reader2
    
    t_S1 = tab_reader( 'S1_' + name, dir_name)
    v_n1 = tab_reader2( 'n1_' + name, dir_name)
   
    t_S2 = tab_reader( 'S2_' + name, dir_name)
    v_n2 = tab_reader2( 'n2_' + name, dir_name)
    
    t_start = t_start(t_S1, eps, N1)
    
    S_mean1 = asymptotic_S_1(t_S1, eps, N1, flag = True, t_start = t_start)
    S_mean2 = asymptotic_S_1(t_S2, eps, N2, flag = True, t_start = t_start)
    
    
    from my_print import my_pyplot
    if rip == 1:
        print('Eseguo my_pyplot.')
        info_1 = {'xlab' : 'Tempo tau [step/N]', 'ylab1' : 'Numero specie S1', 
                  'ylab2': 'Numero specie S2', 
                  'tit1' : 'S1('+u"\u03C4"+') random per '+u"\u03B5"+' = '+repr(eps),
                  'tit2' : 'S2('+u"\u03C4"+') random per '+u"\u03B5"+' = '+repr(eps) }
        my_pyplot('S1_' + name, 'S2_' + name, dir_name, info_1)
    
    #Pn1 = Pn(v_n1, N1, t_start)
    Pn1 = Pn_cumulative2(v_n1, N1, t_start)
    #Pn2 = Pn(v_n2, N2, t_start)
    Pn2 = Pn_cumulative2(v_n2, N2, t_start)
    
        
    simulation_t = round((time.time() - start_time)/60,2)
    #print("Tempo simulazione: {}".format(simulation_t), 'min.')
   
    #print("one_simulation eseguita con successo. \n")
    
    return (S_mean1, S_mean2, Pn1, Pn2, simulation_t)

def N_one_simulation(N1 = 50, N2 = 50, S1 = 10, S2 = 10, eps = 0.05, p = 0.33, 
                     t = 1000, dir_name = '50-50', rip = 1, g=1, flag = False):
    from one_step_bi import one_step
    from random import randint
    from copy import deepcopy
    import time
    start_time = time.time()
    name = 'N-'+format(p,'.2f') +'-'+repr(eps)+'-'+repr(rip)
    
    from matrici import adjacency_matrix_nested
    A = adjacency_matrix_nested(S1, S2, p , dir_name, rip, g, flag)
    #print('A = ', A)
    tau_max1 = int(t/N1)
   
    v1 = [ randint(0, S1-1) for x in range (0,N1)]
    n1 = []
    Smax1 = max(v1)
    for i in range (0,Smax1+1):
        c1 = v1.count(i)
        n1.append(c1)
    #print('n1[0] = ', n1[0])    
    #print('n1[-1] = ', n1[-1])
    v2 = [ randint(0, S2-1) for x in range (0,N2)]
    n2 = []
    Smax2 = max(v2)
    for i in range (0,Smax2+1):
        c2 = v2.count(i)
        n2.append(c2)
    #print('n2[0] = ', n2[0])    
    #print('n2[-1] = ', n2[-1])
    from my_print import print_tuple
    
    #t_conv = 0
    S_range_1 = 0
    S_range_2 = 0
    for i in range (1,tau_max1):
        #qui il programma è un po' imparziale, perchè tratta la specie 1 come standard
        for k in range(0,N1):
            (v1, v2, n1, n2) = one_step(N1, N2, v1, v2, n1, n2, A, eps)
            #(v1, v2, n1, n2) = one_step(N1, N2, v1, v2, n1, n2, A, eps, rip, True, dir_name)
        n_1 = deepcopy(n1)
        S1 = len(n_1) - n_1.count(0)
        print_tuple([i,S1], 'S1_'+name, dir_name)
        print_tuple(n_1, 'n1_'+name, dir_name, d = len(n_1))
        if S_range_1 < S1:
            S_range_1 = S1
        n_2 = deepcopy(n2)
        S2 = len(n_2) - n_2.count(0)
        print_tuple([i,S2], 'S2_'+name, dir_name)
        print_tuple(n_2, 'n2_'+name, dir_name, d = len(n_2))
        if S_range_2 < S2:
            S_range_2 = S2

    
    #from my_print import print_tuple3
    #from my_print import print_gnuplot, print_gnuplot3, print_gnuplot_sys 
    from data_analysis import asymptotic_S_1, Pn, t_start, Pn_cumulative2
    from my_print import tab_reader
    from my_print import tab_reader2
    
    t_S1 = tab_reader( 'S1_' + name, dir_name)
    v_n1 = tab_reader2( 'n1_' + name, dir_name)
    #print('v_n1 = ', v_n1 )
    t_S2 = tab_reader( 'S2_' + name, dir_name)
    v_n2 = tab_reader2( 'n2_' + name, dir_name)
    
    t_start = t_start(t_S1, eps, N1)
    #qui è da cambiare la parte in eps-nu
    S_mean1 = asymptotic_S_1(t_S1, eps, N1)
    S_mean2 = asymptotic_S_1(t_S2, eps, N2)
    #print('j = {}'.format(j))
    
    from my_print import my_pyplot
    if rip == 1:
        print('Eseguo my_pyplot.')
        info_1 = {'xlab' : 'Tempo '+u"\u03C4"+' [step/N]', 'ylab1' : 'Numero specie S1', 
                  'ylab2': 'Numero specie S2', 
                  'tit1' : 'S1('+u"\u03C4"+') per '+u"\u03B5"+' = '+repr(eps),
                  'tit2' : 'S2('+u"\u03C4"+') per '+u"\u03B5"+' = '+repr(eps) }
        my_pyplot('S1_' + name, 'S2_' + name, dir_name, info_1)
    
    #Pn1 = Pn(v_n1, N1, t_start)
    Pn1 = Pn_cumulative2(v_n1, N1, t_start)
    #Pn2 = Pn(v_n2, N2, t_start)
    Pn2 = Pn_cumulative2(v_n2, N2, t_start)
  
        
        
    simulation_t = round((time.time() - start_time)/60,2)
    print("Tempo simulazione: {}".format(simulation_t), 'min.')
   
    return (S_mean1, S_mean2, Pn1, Pn2, simulation_t)

