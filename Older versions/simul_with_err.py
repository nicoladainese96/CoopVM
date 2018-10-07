def R_simul_with_err(N1=100, N2=100, rip = 10, p = 0.33, t=10000, dir_name = '', R_start_time = 0):
    from one_simulation_vecchia import R_one_simulation
    import my_print as my
    import math
    import time
    import statistics
    import numpy as np 
    
    start = time.time()
    S1 = int(math.sqrt(N1))
    S2 = int(math.sqrt(N2))
    print("S1 = {}".format(S1))
    print("S2 = {}".format(S2), '\n')
    
    name = dir_name+'/R-'+format(p,'.2f') #dir_name
    #name = repr(N1)+'-'+repr(N2)+'-'+repr(rip)+'/N-'+format(p,'.2f')
    #name2 = 'N-'+format(p,'.2f')
    eps_S = []
    #kappas = np.linspace(0, 0.7, 8)
    epsilons = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    #for i in range(len(kappas)):
    #    eps1 = (kappas[i]/(1-kappas[i]))/(p*math.sqrt(N1))
    #    epsilons.append(round(eps1,4))
    print('Valori di epsilon da analizzare = ', epsilons)    
    
    print('Numero di simulazioni per ciascuno = ', rip, '\n')
    for i in range(len(epsilons)):
        eps = epsilons[i]
        #my.guess(N1, S1, p, eps, name)
        S_list = ([], [])
        m_Pn1 =  [ [] for x in range(0,N1)]
        m_Pn2 =  [ [] for x in range(0,N2)]
        mean_Pn1 = []
        s_Pn1 = []
        mean_Pn2 = []
        s_Pn2 = []
        v_t_tot = []
        
        for j in range(rip):
            print("R - Simulazione {} numero {} con eps = {}".format(i+1, j+1,eps))
            (S_mean1, S_mean2, Pn1, Pn2, t_one_simul) = R_one_simulation(N1, N2, S1, S2, eps, p, t, name, j+1, i+1)
            
            #stronzate sul tempo
            tot_time = round(220*t_one_simul + R_start_time,2)
            v_t_tot.append(tot_time)
            remaining_t = round(statistics.mean(v_t_tot)/3 - R_start_time - (time.time()-start)/60,2)
            print('Tempo totale stimato = ', round(statistics.mean(v_t_tot)/3,2), 'min')
            print('Tempo rimanente stimato = ', remaining_t, 'min \n')
            
            
            for k in range(len(Pn1)):
                m_Pn1[k].append(Pn1[k])
    
            for k in range(len(Pn2)):
                m_Pn2[k].append(Pn2[k])
   
            S_list[0].append(S_mean1)
            S_list[1].append(S_mean2)
        info_hist = {'xlab' : 'Numero individui n', 
                     'ylab_1' : 'Probabilità cumulata P1>(n)', 
                     'tit1' : 'Specie I gruppo con eps = '+repr(eps),
                     'ylab_2' : 'Probabilità cumulata P2>(n)', 
                     'tit2' : 'Specie II gruppo con eps = '+repr(eps)}
        #info_hist_2 = {'xlab' : 'n', 'ylab_2' : 'Densità di prob P2', 'tit2' : 'PDF specie II gruppo con eps = '+repr(eps) }
        for k in range(N1):
            mean_Pn1.append(statistics.mean(m_Pn1[k]))
            if len(m_Pn1[k]) > 1:
                radN = math.sqrt(len(m_Pn1[k]))
                s_Pn1.append(statistics.stdev(m_Pn1[k])/radN)
            else:
                s_Pn1.append(math.sqrt(m_Pn1[k]))
       
        #my.plot_hist(mean_Pn1, name2+'-'+repr(eps)+'-I', name, info_hist_1)
        
        for k in range(N2):
            mean_Pn2.append(statistics.mean(m_Pn2[k])) 
            if len(m_Pn2[k]) > 1:
                radN = math.sqrt(len(m_Pn2[k]))
                s_Pn2.append(statistics.stdev(m_Pn2[k])/radN)
            else:
                s_Pn2.append(math.sqrt(m_Pn2[k]))
        
        #my.plot_hist(mean_Pn1, mean_Pn2, s_Pn1, s_Pn2, name2+'-'+repr(eps), name, info_hist)
        
        info_hist2 = {'xlab' : 'Numero individui n', 
                     'ylab_1' : 'Probabilità cumulata P1>(n)', 
                     'tit1' : 'Specie I gruppo con eps = '+repr(eps),
                     'ylab_2' : 'Probabilità cumulata P2>(n)', 
                     'tit2' : 'Specie II gruppo con eps = '+repr(eps)}
        #my.plot_hist2(name2+'-'+repr(eps), name, rip, N1, N2, info_hist2)
        
        S_mean_1 = statistics.mean(S_list[0])
        S_dev_1 = statistics.stdev(S_list[0])
        if S_dev_1 == 0:
            S_dev_1 = 0.001
            
        S_mean_2 = statistics.mean(S_list[1])
        S_dev_2 = statistics.stdev(S_list[1])
        if S_dev_2 == 0:
            S_dev_2 = 0.001
        
        eps_S.append((eps, S_mean_1, S_dev_1, S_mean_2, S_dev_2 ))
        
        
    
    #info_eps = {'tit': 'S(epsilon) per simulazione ' + name2, 'xlab': 'epsilon' , 'ylab_1': 'S_1', 'ylab_2' : 'S_2'}
    #my.eps_print(eps_S, name2, name, info_eps)
    #finish = time.time()
    #t_tot = round((finish-start)/60,2)
    #print("Tempo totale impiegato = {}".format(t_tot), 'min')
    return eps_S

def N_simul_with_err(N1=100, N2=100, rip = 10, p = 0.33,  t=10000, dir_name = '', N_start_time = 0):
    from one_simulation_vecchia import N_one_simulation
    import my_print as my
    import math
    import time
    import statistics
    import numpy as np
    
    start = time.time()
    S1 = int(math.sqrt(N1))
    S2 = int(math.sqrt(N2))
    print("S1 = {}".format(S1))
    print("S2 = {}".format(S2), '\n')
    
    name = dir_name+'/N-'+format(p,'.2f')
    #name = repr(N1)+'-'+repr(N2)+'-'+repr(rip)+'/N-'+format(p,'.2f')
    #name2 = 'N-'+format(p,'.2f')
    
    #eps = 0
    eps_S = []
    #kappas = [0, 0.05, 0.33, 0.51, 0.66]
    #kappas = np.linspace(0, 0.7, 8)
    epsilons = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    #for i in range(len(kappas)):
    #    eps1 = (kappas[i]/(1-kappas[i]))/(p*math.sqrt(N1))
    #    epsilons.append(round(eps1,4))
        
    print('Valori di epsilon da analizzare = ', epsilons)    
    
    print('Numero di simulazioni per ciascuno = ', rip, '\n')
    v_t_tot = []
    for i in range(len(epsilons)):
        eps = epsilons[i]
        S_list = ([], [])
        m_Pn1 =  [ [] for x in range(0,N1)]
        m_Pn2 =  [ [] for x in range(0,N2)]
        mean_Pn1 = []
        mean_Pn2 = []
        s_Pn1 = []
        s_Pn2 = []
        
        for j in range(0,rip):
            print("N - Simulazione {} numero {} con eps = {}".format(i+1,j+1,eps))
            #(S_mean1, S_mean2, Pn1, Pn2) = N_one_simulation(N1, N2, S1, S2, eps, p, t, name, j+1)
            (S_mean1, S_mean2, Pn1, Pn2, t_one_simul) = N_one_simulation(N1, N2, S1, S2, eps, p, t, name, j+1, i+1)
            
            tot_time = round(220*t_one_simul + N_start_time,2)
            v_t_tot.append(tot_time)
            remaining_t = round(statistics.mean(v_t_tot)/3 - N_start_time - (time.time()-start)/60,2)
            print('Tempo totale stimato = ', round(statistics.mean(v_t_tot)/3,2), 'min')
            print('Tempo rimanente stimato = ', remaining_t, 'min \n')
            for k in range(len(Pn1)):
                m_Pn1[k].append(Pn1[k])
            for k in range(len(Pn2)):
                m_Pn2[k].append(Pn2[k])
   
            S_list[0].append(S_mean1)
            S_list[1].append(S_mean2)
        info_hist = {'xlab' : 'Numero individui n', 'ylab_1' : 'Densità di prob P1',
                     'tit1' : 'PDF specie I gruppo con eps = '+repr(eps),
                     'ylab_2' : 'Densità di prob P2', 
                     'tit2' : 'PDF specie II gruppo con eps = '+repr(eps)}
        #fare un unico istogramma
        for k in range(N1):
            mean_Pn1.append(statistics.mean(m_Pn1[k]))
            if len(m_Pn1[k]) > 1:
                #correggere err media
                s_Pn1.append(statistics.stdev(m_Pn1[k]))
            else:
                s_Pn1.append(math.sqrt(m_Pn1[k]))
        #my.plot_hist(mean_Pn1, name2+'-'+repr(eps)+'-I', name, info_hist_1)
        
        for k in range(N2):
            mean_Pn2.append(statistics.mean(m_Pn2[k])) 
            if len(m_Pn2[k]) > 1:
                #correggere err media
                s_Pn2.append(statistics.stdev(m_Pn2[k]))
            else:
                s_Pn2.append(math.sqrt(m_Pn2[k]))
        #my.plot_hist(mean_Pn1, mean_Pn2, s_Pn1, s_Pn2, name2+'-'+repr(eps), name, info_hist)
    
        S_mean_1 = statistics.mean(S_list[0])
        S_dev_1 = statistics.stdev(S_list[0])
        if S_dev_1 == 0:
            S_dev_1 = 0.001
            
        S_mean_2 = statistics.mean(S_list[1])
        S_dev_2 = statistics.stdev(S_list[1])
        if S_dev_2 == 0:
            S_dev_2 = 0.001
        
        eps_S.append((eps, S_mean_1, S_dev_1, S_mean_2, S_dev_2 ))
        
    
    return eps_S


