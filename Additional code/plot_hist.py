# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 10:25:11 2018

@author: Utente
"""
def replot_hist():
    import my_print as my
    import numpy as np
    import math
    p = 0.4
    dir_name = '100-100-100/R-0.40'
    rip = 100
    N1 = 100
    N2 = 100
    kappas = np.linspace(0, 0.7, 8)
    epsilons = []
    for i in range(len(kappas)):
        eps1 = (kappas[i]/(1-kappas[i]))/(p*math.sqrt(N1))
        epsilons.append(round(eps1,4))
    for eps in epsilons:
        name = 'R-0.40-'+repr(eps)
    
        info = {'xlab' : 'Numero individui n', 
                         'ylab_1' : 'Probabilità cumulata P1>(n)', 
                         'tit1' : 'Specie I gruppo con eps = '+repr(eps),
                         'ylab_2' : 'Probabilità cumulata P2>(n)', 
                         'tit2' : 'Specie II gruppo con eps = '+repr(eps)}
        my.plot_hist2(name, dir_name, rip, N1, N2, info)
    
    print('Tester2 eseguito con successo.')

