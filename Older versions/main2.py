# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 12:19:12 2018

@author: Utente
"""

def main2(N1 = 50, N2 = 50, p = 0.4, rip = 10):
    from simul_with_err2 import simul_with_err2
    from init_simulation import init_simulation
    import statistics
    import time
    #import my_print as my
    #import math
    start = time.time()
    #dir_name = repr(N1)+'-'+repr(N2)
    #name = 'p'+format(p,'.2f')
    #S1 = int(math.sqrt(N1))
    #S2 = int(math.sqrt(N2))
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
    
    #ESEGUO SIMULAZIONE CON RIPETIZIONI
    simul_with_err2(N1, N2, rip, p, tot_step)