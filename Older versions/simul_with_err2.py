# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 12:19:53 2018

@author: Utente
"""
def simul_with_err2 (N1=100, N2=100, rip = 10, p = 0.33, t=10000):
    from one_simulation import R_one_simulation, N_one_simulation
    from data_analysis import asymptotic_deg_n
    import my_print as my
    import math
    import time
    #import statistics as st
    
    start = time.time()
    S1 = int(math.sqrt(N1))
    S2 = int(math.sqrt(N2))
    print("S1 = {}".format(S1))
    print("S2 = {}".format(S2), '\n')
    eps = 0.5
    #eps = 1
    dir_name = repr(N1)+'-'+repr(N2)+'-'+repr(rip)+'-'+repr(eps)+'-'+repr(p)+'-b'
    
    #my.guess(N1, S1, p, eps, dir_name)
   
    for i in range(0,rip): 
        #assicurarsi che stampi bene i documenti deg per ogni i
        R_one_simulation(N1, N2, S1, S2, eps, p, t, dir_name, i, flag = True)
        N_one_simulation(N1, N2, S1, S2, eps, p, t, dir_name, i, flag = True)
        print('Simulazione numero {} eseguita. \n'.format(i+1))
    tau_start = int(t/(2*N1))
    
    N_deg_n1 = []
    N_deg_n2 = []
    R_deg_n1 = []
    R_deg_n2 = []
    for i in range(rip):
        name1 = 'n1_N-'+format(p,'.2f')+'-'+repr(eps)+'-'+repr(i)
        name2 = 'deg1_N-'+repr(i)
        deg_n1 = asymptotic_deg_n(N1, name1, name2, dir_name, tau_start)
        #if i == 0:
        #    print('deg_n1 = ', deg_n1, '\n')
        N_deg_n1.append(deg_n1)
        name3  = 'n2_N-'+format(p,'.2f')+'-'+repr(eps)+'-'+repr(i)
        name4 = 'deg2_N-'+repr(i)
        deg_n2 = asymptotic_deg_n(N2, name3, name4, dir_name, tau_start)
        #if i == 0:
        #    print('deg_n2 = ', deg_n2, '\n')
        N_deg_n2.append(deg_n2)
    #print('N_deg_n1 = ', N_deg_n1, '\n') 
    #print('N_deg_n2 = ', N_deg_n2, '\n')   
    
    for i in range(0,rip):
        name1 = 'n1_R-'+format(p,'.2f')+'-'+repr(eps)+'-'+repr(i)
        name2 = 'deg1_R-'+repr(i)
        deg_n1 = asymptotic_deg_n(N1, name1, name2, dir_name, tau_start)
        R_deg_n1.append(deg_n1)
        name3  = 'n2_R-'+format(p,'.2f')+'-'+repr(eps)+'-'+repr(i)
        name4 = 'deg2_R-'+repr(i)
        deg_n2 = asymptotic_deg_n(N2, name3, name4, dir_name, tau_start)
        R_deg_n2.append(deg_n2)
    
    N_deg_x1 = deg_x(N_deg_n1, S1, S2, rip)

    N_deg_x2 = deg_x(N_deg_n2, S2, S1, rip)
    
    R_deg_x1 = deg_x(R_deg_n1, S1, S2, rip)
   
    R_deg_x2 = deg_x(R_deg_n2, S2, S1, rip)
   
    info1 = { 'xlab_1': 'Numero di connessioni (deg) per S1 = '+repr(S1), 
             'xlab_2' : 'Numero di connessioni (deg) per S2 = '+repr(S2),
             'ylab_1': 'Abbondanza relativa specie I gruppo ( <x> )', 
             'ylab_2': 'Abbondanza relativa specie II gruppo ( <x> )'}
    
    name = repr(rip)
    my.print_deg_x(N_deg_x1, N_deg_x2, R_deg_x1, R_deg_x2, name, dir_name, info1, S1, S2)
    finish = time.time()
    total_time = round((finish-start)/60 , 2)
    my.overview2(N1, S1, eps, p, rip,total_time, dir_name)
    
    
def deg_x (deg_n, S1, S2, rip):
    import statistics as st
    import math
    #attenzione S1 è S1 per n1, S2 per n2 e lo stesso per S2
    deg_x = []
   # k_max = 0
    m_deg_x = []
    s_deg_x = []
    kappas = []
    #problema: k può essere anche = S2!! -> corretto, controllare index range
    for k in range(S2+1):
        k_x = []
        for j in range(rip):
            for i in range(S1):
                if deg_n[j][i][0] == k:
                    k_x.append(deg_n[j][i][1])
        #rivedere se l'istruzione ha senso
        if len(k_x) > 1:
            m_deg_x.append(st.mean(k_x))
            N = len(k_x)
            s_deg_x.append(st.stdev(k_x)/math.sqrt(N))
            kappas.append(k)
            #if k > k_max:
            #    k_max = k
    
    #kappas = [x for x in range(k_max) ]
    deg_x = (kappas, m_deg_x, s_deg_x)
    #print('kappas = ', kappas)
    return deg_x
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def simul_with_err2_vecchia (N1=100, N2=100, p = 0.33, t=10000, rip = 10):
    from one_simulation import R_one_simulation, N_one_simulation
    import my_print as my
    import math
    #import time
    import statistics
    
    #start = time.time()
    S1 = int(math.sqrt(N1))
    S2 = int(math.sqrt(N2))
    print("S1 = {}".format(S1))
    print("S2 = {}".format(S2), '\n')
    dir_name = repr(N1)+'-'+repr(N2)+'-b'
    
    eps = 1
    R_S_list = ([], [])
    R_m_Pn1 =  [ [] for x in range(0,N1)]
    R_m_Pn2 =  [ [] for x in range(0,N2)]
    R_mean_Pn1 = []
    R_mean_Pn2 = []
    
    
    N_S_list = ([], [])
    N_m_Pn1 =  [ [] for x in range(0,N1)]
    N_m_Pn2 =  [ [] for x in range(0,N2)]
    N_mean_Pn1 = []
    N_mean_Pn2 = []
    for i in range(0,rip):
        (R_S_mean1, R_S_mean2, R_Pn1, R_Pn2, simulation_t) = R_one_simulation(N1, N2, S1, S2, eps, p, t, dir_name, i+1, flag = True)
        (N_S_mean1, N_S_mean2, N_Pn1, N_Pn2, simulation_t) = N_one_simulation(N1, N2, S1, S2, eps, p, t, dir_name, i+1, flag = True)
        
        
        for k in range(len(N_Pn1)):
                N_m_Pn1[k].append(N_Pn1[k])
        for k in range(len(N_Pn2)):
                N_m_Pn2[k].append(N_Pn2[k])
   
        N_S_list[0].append(N_S_mean1)
        N_S_list[1].append(N_S_mean2)
        
    
    
        for k in range(len(R_Pn1)):
                R_m_Pn1[k].append(R_Pn1[k])
        for k in range(len(R_Pn2)):
                R_m_Pn2[k].append(R_Pn2[k])
       
        R_S_list[0].append(R_S_mean1)
        R_S_list[1].append(R_S_mean2)
    
    N_info_hist = {'xlab' : 'Numero individui n', 'ylab_1' : 'Densità di prob P1', 'tit1' : 'PDF specie I gruppo nested con eps = '+repr(eps),
                   'ylab_2' : 'Densità di prob P2', 'tit2' : 'PDF specie II gruppo nested con eps = '+repr(eps)}
    R_info_hist = {'xlab' : 'Numero individui n', 'ylab_1' : 'Densità di prob P1', 'tit1' : 'PDF specie I gruppo random con eps = '+repr(eps),
                   'ylab_2' : 'Densità di prob P2', 'tit2' : 'PDF specie II gruppo random con eps = '+repr(eps)}
    
    for k in range(N1):
        N_mean_Pn1.append(statistics.mean(N_m_Pn1[k]))
    
    for k in range(N2):
        N_mean_Pn2.append(statistics.mean(N_m_Pn2[k])) 
    
    my.plot_hist(N_mean_Pn1, N_mean_Pn2, 'N', dir_name, N_info_hist)

    N_S_mean_1 = statistics.mean(N_S_list[0])
    N_S_dev_1 = statistics.stdev(N_S_list[0])
    if N_S_dev_1 == 0:
        N_S_dev_1 = 0.001
        
    N_S_mean_2 = statistics.mean(N_S_list[1])
    N_S_dev_2 = statistics.stdev(N_S_list[1])
    if N_S_dev_2 == 0:
        N_S_dev_2 = 0.001
        
    for k in range(N1):
        R_mean_Pn1.append(statistics.mean(R_m_Pn1[k]))
    
    for k in range(N2):
        R_mean_Pn2.append(statistics.mean(R_m_Pn2[k])) 
    
    my.plot_hist(R_mean_Pn1, R_mean_Pn2, 'R', dir_name, R_info_hist)

    R_S_mean_1 = statistics.mean(R_S_list[0])
    R_S_dev_1 = statistics.stdev(R_S_list[0])
    if R_S_dev_1 == 0:
        R_S_dev_1 = 0.001
        
    R_S_mean_2 = statistics.mean(R_S_list[1])
    R_S_dev_2 = statistics.stdev(R_S_list[1])
    if R_S_dev_2 == 0:
        R_S_dev_2 = 0.001
    
    
    N_eps_S = (eps, N_S_mean_1, N_S_dev_1, N_S_mean_2, N_S_dev_2 )
    R_eps_S = (eps, R_S_mean_1, R_S_dev_1, R_S_mean_2, R_S_dev_2 )
    
    return (N_eps_S, R_eps_S)
        


    
  