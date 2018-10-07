# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 09:51:26 2018

@author: Utente
"""

#old main
def main_simulation(N1 = 100, N2 = 100, rip = 10, p = 0.33, parent_dir = 'C:/Users/Utente/Anaconda3/Cooperazione'):
    from simul_with_err import R_simul_with_err, N_simul_with_err
    from init_simulation import init_simulation
    import statistics
    import time
    import my_print as my
    import math
    import numpy as np
    start = time.time()
    dir_name = parent_dir + '/'+ repr(N1)+'-'+repr(N2)+'-'+repr(rip)
    name = 'p'+format(p,'.2f')
    S1 = int(math.sqrt(N1))
    S2 = int(math.sqrt(N2))
    print('Calcolo il tempo medio di assorbimento...')
    # CALCOLO IL TEMPO MEDIO DI ASSORBIMENTO/CONVERGENZA A N FISSATO
    t = []
    for i in range(0,5):
        t_conv = init_simulation(N1)
        t.append(t_conv)
    t_mean = int(statistics.mean(t))
    print('t_mean = {}'.format(t_mean))
    #attenzione qui che potrebbe essere un tempo spropositato
    tot_step = int(t_mean)*10
    finish = time.time()
    t_tot = round((finish-start)/60,2)
    print('Tempo impiegato per calcolare t_conv = {}'.format(t_tot), 'min\n')
    
    t0 = time.time()
    
    #RANDOM SIMULATION
    R_start_time = round((time.time() - start)/60,2)
    print('R_start_time = ', R_start_time)
    R_eps_S = R_simul_with_err(N1, N2,rip, p, tot_step, dir_name, R_start_time = R_start_time)
    t2 = time.time()
    t_seconda = round((t2 - t0)/60 , 2)
    print('Tempo esecuzione simulazioni random = {}'.format(t_seconda), 'min\n')
    
    #NESTED SIMULATION
    N_start_time = round((time.time()-start)/60,2)
    print('N_start_time = ', N_start_time)
    N_eps_S = N_simul_with_err(N1, N2, rip, p, tot_step, dir_name, N_start_time = N_start_time)
    t3 = time.time()
    t_N = round((t3-t2)/60,2)
    print('Tempo esecuzione simulazioni nested = {}'.format(t_N), 'min\n')
    
    #plot finali
    #info1 = {'tit1': 'S(eps) nested con C = 0.35', 'tit2': 'S(eps) random con C = 0.35',
    #        'xlab': 'epsilon' , 'ylab_1': 'S_1', 'ylab_2' : 'S_2'}
    #info2 = {'tit' : '(S_nest - S_rnd)/S0 in funzione di eps per C = 0.35',
    #         'ylab_3' : '(delta S1)/S0', 'ylab_4': 'delta S2'}
    #my.eps_print(R_eps_S, N_eps_S, name, dir_name, info1, info2, S1, S2)
    #u"\u03C4" tau
    N_info = {'ylab' : 'Abbondanze n delle S1 specie', 'tit': 'n('+u"\u03C4"+') per '}
    R_info = {'ylab' : 'Abbondanze n delle S2 specie', 'tit': 'n('+u"\u03C4"+') per '}
    #kappas = np.linspace(0, 0.7, 8)
    #epsilons = []
    #for i in range(len(kappas)):
    #    eps1 = (kappas[i]/(1-kappas[i]))/(p*math.sqrt(N1))
    #    epsilons.append(round(eps1,4))
    epsilons = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    my.n_plot(dir_name, format(p,'.2f'), epsilons, N_info, R_info)
    
    t_f = time.time()
    t_simul = round((t_f-start)/60,2)
    my.overview(N1, tot_step, rip, t_simul, dir_name)
    print('main eseguita con successo. \n')

#only this function needed
def tau_conv(N):
    from init_simulation import init_simulation
    import statistics as stat
    tau = []
    for i in range(5):
        tau_i = init_simulation(N)
        tau.append(tau_i)
    tau_mean = stat.mean(tau)
    tau_dev = stat.stdev(tau)
    print('tau_mean = ', round(tau_mean,1))
    print('tau_dev = ', round(tau_dev,1))
    tau_conv = int(round(tau_mean + 10*tau_dev, 0))
    print('tau_conv = tau_mean + 5*tau_dev = ', tau_conv, '\n')
    
    return tau_conv