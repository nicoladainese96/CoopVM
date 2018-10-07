# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 08:30:32 2018
Used both in the simulation and the analysis part. It should be splitted in two parts.
@author: nicola.dainese96@gmail.com
"""

def print_matrix(A, S1, S2, C, filename, parent_dir):
    import matplotlib.pyplot as plt
    from ensure_dir import ensure_dir
    import os
    script_dir = os.getcwd()
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(A, cmap = 'Greys')
    ax.set_title('Matrice interazioni con dati reali e connettanza = {}'.format(C))
    ax.set_xlabel('Numero specie piante: S2 = {}'.format(S2))
    ax.set_ylabel('Numero specie impollinatori: S1 = {}'.format(S1))
    
    xtics = [x-0.5 for x in range(0,S2+1)]
    ytics = [x-0.5 for x in range(0,S1+1)]
    ax.grid()
    ax.set_yticks(ytics)
    ax.set_xticks(xtics)
    plt.setp(ax.get_xticklabels(), visible=False)
    plt.setp(ax.get_yticklabels(), visible=False)
    
    path = parent_dir+'/'+filename+'//prova.txt'
    ensure_dir(path)
    directory = os.path.dirname(path)
    os.chdir(directory)
    fig.savefig(filename+'_matrix.png')
    plt.close()
    os.chdir(script_dir)
    
def print_matrix2(A, S1, S2, C, NODF, re, parent_dir):
    import matplotlib.pyplot as plt
    from ensure_dir import ensure_dir
    import os
    script_dir = os.getcwd()
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(A, cmap = 'Greys')
    ax.set_title('Matrice per step {} con C = {} e NODF = {}'.format(re, C, NODF))
    ax.set_xlabel('S2 = {}'.format(S2))
    ax.set_ylabel('S1 = {}'.format(S1))
    
    xtics = [x-0.5 for x in range(0,S2+1)]
    ytics = [x-0.5 for x in range(0,S1+1)]
    ax.grid()
    ax.set_yticks(ytics)
    ax.set_xticks(xtics)
    plt.setp(ax.get_xticklabels(), visible=False)
    plt.setp(ax.get_yticklabels(), visible=False)
    
    path = parent_dir+'//prova.txt'
    ensure_dir(path)
    directory = os.path.dirname(path)
    os.chdir(directory)
    fig.savefig(repr(C)+'-'+repr(re)+'_matrix.png')
    plt.close()
    os.chdir(script_dir)
    
def print_list_csv(l, name, dir_name, rnd =2, d = 2):
    from ensure_dir import ensure_dir
    file_path = dir_name+'//data_plot//'+ name + '.csv'
    ensure_dir(file_path)
    with open(file_path, 'a') as f:
        if d >1:
            for i in range(0,d-1):
                print("{},".format(round(l[i],rnd)), end ='', file = f)
            print("{}".format(round(l[d-1],rnd)), file = f)
        else:
            print(l, file = f)
        
def info_p(N, rip, eps, ps, t, work_dir, parent_dir):
    from ensure_dir import ensure_dir
    file_path = work_dir+'/info_p.csv'
    ensure_dir(file_path)
    with open(file_path, 'a') as f:
        print(parent_dir, N, rip, eps, sep = ',', end = '', file = f)
        for i in range(len(ps)-1):
            print( '',ps[i], sep = ',', end = '', file = f)
        print( '',ps[-1], t, sep = ',', file = f)
    
def info_e( N, rip, epsilons, p, t, work_dir, parent_dir):
    from ensure_dir import ensure_dir
    file_path = work_dir+'/info_e.csv'
    ensure_dir(file_path)
    with open(file_path, 'a') as f:
        print(parent_dir, N, rip,  sep = ',', end = '', file = f)
        for i in range(len(epsilons)-1):
            print( '',epsilons[i], sep = ',', end = '', file = f)
        print( '',epsilons[-1], p, t, sep = ',', file = f)
    
def info_NODF( N, rip, NODFs, eps, p, t, work_dir, parent_dir):
    from ensure_dir import ensure_dir
    file_path = work_dir+'/info_NODF.csv'
    ensure_dir(file_path)
    with open(file_path, 'a') as f:
        print(parent_dir, N, rip,  sep = ',', end = '', file = f)
        for i in range(len(NODFs)-1):
            print( '',NODFs[i], sep = ',', end = '', file = f)
        print( '',NODFs[-1], eps, p, t, sep = ',', file = f)

def info_precision( N, rip, NODFs, eps, p, t, work_dir, parent_dir):
    from ensure_dir import ensure_dir
    file_path = work_dir+'/info_precision.csv'
    ensure_dir(file_path)
    with open(file_path, 'a') as f:
        print(parent_dir, N, rip,  sep = ',', end = '', file = f)
        for i in range(len(NODFs)-1):
            print( '',NODFs[i], sep = ',', end = '', file = f)
        print( '',NODFs[-1], eps, p, t, sep = ',', file = f)
        
def N_print_info_csv(eps, p, rip, dir_name, parent_dir):
    n1 = dir_name
    n2 = dir_name
    S1 = dir_name
    S2 = dir_name
    for i in range (rip):
        file_name = repr(eps)+'-'+repr(p)+'-'+repr(rip)+'-'+repr(i)+'.csv'
        n1 = n1+',N_n1_'+file_name
        n2 = n2+',N_n2_'+file_name
        S1 = S1+',N_S1_'+file_name
        S2 = S2+',N_S2_'+file_name
    print_string_csv(n1, 'N_n1_', parent_dir)
    print_string_csv(n2, 'N_n2_', parent_dir)
    print_string_csv(S1, 'N_S1_', parent_dir)
    print_string_csv(S2, 'N_S2_', parent_dir)
    
def R_print_info_csv(eps, p, rip, dir_name, parent_dir):
    n1 = dir_name
    n2 = dir_name
    S1 = dir_name
    S2 = dir_name
    for i in range (rip):
        file_name = repr(eps)+'-'+repr(p)+'-'+repr(rip)+'-'+repr(i)+'.csv'
        n1 = n1+',R_n1_'+file_name
        n2 = n2+',R_n2_'+file_name
        S1 = S1+',R_S1_'+file_name
        S2 = S2+',R_S2_'+file_name
    print_string_csv(n1, 'R_n1_', parent_dir)
    print_string_csv(n2, 'R_n2_', parent_dir)
    print_string_csv(S1, 'R_S1_', parent_dir)
    print_string_csv(S2, 'R_S2_', parent_dir)
    
def NODF_print_info_csv(NODF, eps, p, rip, dir_name, parent_dir):
    n1 = dir_name
    n2 = dir_name
    S1 = dir_name
    S2 = dir_name
    for i in range (rip):
        file_name = repr(NODF)+'-'+repr(eps)+'-'+repr(p)+'-'+repr(rip)+'-'+repr(i)+'.csv'
        n1 = n1+',n1_'+file_name
        n2 = n2+',n2_'+file_name
        S1 = S1+',S1_'+file_name
        S2 = S2+',S2_'+file_name
    print_string_csv(n1, 'n1_', parent_dir)
    print_string_csv(n2, 'n2_', parent_dir)
    print_string_csv(S1, 'S1_', parent_dir)
    print_string_csv(S2, 'S2_', parent_dir)
        
def print_string_csv(string, name, dir_name):
    from ensure_dir import ensure_dir
    file_path = dir_name+'//'+ name + 'files.csv'
    ensure_dir(file_path)
    with open(file_path, 'a') as f:
        print(string, file = f)
        
def eps_print(eps, S_mean_1N, S_dev_1N, S_mean_2N, S_dev_2N, 
              S_mean_1R, S_dev_1R, S_mean_2R, S_dev_2R, 
              name, dir_name, S1, S2, C):
    import matplotlib.pyplot as plt
    import math
    #NOTE: 'seaborn' is not the original style that you find in matplotlib!
    #create a style in a more flexible way -> seaborn was modified by myself
    plt.style.use('seaborn')
    #u"\u03B5"
    #vecchia variabile: eps_S
    #N/R_eps_S = (eps, S_mean_1, S_dev_1, S_mean_2, S_dev_2 )
  
    
    fig, (aa,bb) = plt.subplots(2,2, figsize = (9,8))
    ax1 = aa[0]
    ax2 = aa[1] 
    ax3 = bb[0]
    ax4 = bb[1]
    #[ax1, ax2, ax3, ax4]
    ax1.plot(eps, S_mean_1N, '.')
    ax1.errorbar(eps, S_mean_1N, yerr = S_dev_1N, fmt = 'b.')
    ax1.set_title('S(eps) nested con C = {}'.format(C))
    ax1.set_ylabel('S1 all\'equilibrio con S1 iniziale = {}'.format(S1) )
    ax1.set_xlabel('epsilon') 
    ax1.grid()
    ax1.set_ylim(0)
    ax1.set_autoscale_on(True)
    
    ax3.plot(eps,S_mean_2N, '.')
    ax3.errorbar(eps, S_mean_2N, yerr = S_dev_2N, fmt = 'b.')
    ax3.set_ylabel('S2 all\'equilibrio con S2 iniziale = {}'.format(S2) )
    ax3.set_xlabel('epsilon') 
    ax3.grid() 
    ax3.set_ylim(0)
    ax3.set_autoscale_on(True)
    
    ax2.plot(eps, S_mean_1R, '.')
    ax2.errorbar(eps, S_mean_1R, yerr = S_dev_1R, fmt = 'b.')
    ax2.set_title('S(eps) casuale con C = {}'.format(C))
    ax2.set_ylabel('S1 all\'equilibrio con S1 iniziale = {}'.format(S1))
    ax2.set_xlabel('epsilon') 
    ax2.grid()
    ax2.set_ylim(0)
    ax2.set_autoscale_on(True)
    
    ax4.plot(eps,S_mean_2R, '.')
    ax4.errorbar(eps, S_mean_2R, yerr = S_dev_2R, fmt = 'b.')
    ax4.set_ylabel('S2 all\'equilibrio con S2 iniziale = {}'.format(S2))
    ax4.set_xlabel('epsilon') 
    ax4.grid() 
    ax4.set_ylim(0)
    ax4.set_autoscale_on(True)
    plt.tight_layout()
    
    import os
    path = dir_name
    os.chdir(path)
    fig.savefig('S_eps_'+name+'.png')
    plt.close()
    
    d_S1 = []
    d_S2 = []
    s_S1 = []
    s_S2 = []
    for i in range(len(S_mean_1N)):
        delta1 = (S_mean_1N[i] - S_mean_1R[i])
        s_q1 = math.pow(S_dev_1N[i],2) + math.pow(S_dev_1R[i], 2)
        sigma1 = math.sqrt(s_q1)
        d_S1.append(delta1)
        s_S1.append(sigma1)
        
    for i in range(len(S_mean_2N)):
        delta2 = (S_mean_2N[i] - S_mean_2R[i])
        s_q2 = math.pow(S_dev_2N[i],2) + math.pow(S_dev_2R[i], 2)
        sigma2 = math.sqrt(s_q2)
        d_S2.append(delta2)
        s_S2.append(sigma2)

    fig2, [ax5,ax6] = plt.subplots(2,1, figsize = (6,6))
    
    ax5.plot(eps, d_S1, '.')
    ax5.errorbar(eps, d_S1, yerr = s_S1, fmt = 'b.')
    ax5.set_title('deltaS stazionaria al variare di eps per C = {} '.format(C))
    ax5.set_ylabel('S1 nest - S1 rand con S1 = {}'.format(S1))
    ax5.set_xlabel('epsilon')
    ax5.grid()
    ax5.set_autoscale_on(True)
    
    ax6.plot(eps, d_S2, '.')
    ax6.errorbar(eps, d_S2, yerr = s_S2, fmt = 'b.')
    ax6.set_ylabel('S2 nest - S2 rand con S2 = {}'.format(S2))
    ax6.set_xlabel('epsilon')
    ax6.grid()
    ax6.set_autoscale_on(True)
    plt.tight_layout()
    
    fig2.savefig('deltaS12_eps_'+name+'.png')
    plt.close()
    
    S = []
    d = []
    for i in range(len(d_S1)):
        somma = (d_S1[i] + d_S2[i])/(S1+S2)
        s_q2 = math.pow(s_S1[i],2) + math.pow(s_S2[i], 2)
        err = math.sqrt(s_q2)/(S1+S2)
        S.append(somma)
        d.append(err)
        
    fig3 = plt.figure()
    ax7 = fig3.add_subplot(111)
    ax7.plot(eps, S, '.', label = 'Dati per C = {}'.format(C))
    ax7.errorbar(eps, S, yerr = d, fmt = 'b.')
    #ax7.set_title('deltaS/S0 iniziale al variare di eps per C = {} '.format(C))
    ax7.set_ylabel(r'$(S_{nest} - S_{rand})/S_0$'+' con '+r'$S_0 = {}$'.format(S1+S2))
    ax7.set_xlabel('Intensità di mutualismo '+u"\u03B5")
    #ax7.grid()
    #ax7.set_autoscale_on(True)
    ax7.legend(fontsize = 'large')
    plt.tight_layout()
    
    fig3.savefig('deltaS_eps_'+name+'.png')
    plt.close()
    
    #S_mean_1R, S_dev_1R, S_mean_2R, S_dev_2R
    B = []
    sB = []
    for i in range(len(S_mean_1R)):
        B.append(S_mean_1R[i]+S_mean_2R[i])
        s_q2 = math.pow(S_dev_1R[i],2) + math.pow(S_dev_2R[i], 2)
        err = math.sqrt(s_q2)
        sB.append(err)
       
    fig4 = plt.figure()
    ax8 = fig4.add_subplot(111)
    ax8.plot(eps, B, '.', label = 'Dati per C = {}'.format(C))
    ax8.errorbar(eps, B, yerr = sB, fmt = 'b.')
    #ax8.set_title('Biodiversità S al variare di eps per C = {} '.format(C))
    ax8.set_ylabel(r'$S_{1 rand} + S_{2 rand}$'+' con '+r'$S_0 = {}$'.format(S1+S2))
    ax8.set_xlabel('Intensità di mutualismo '+u"\u03B5")
    #ax8.grid()
    ax8.legend(fontsize = 'large')
    #ax8.set_autoscale_on(True)
    plt.tight_layout()
    
    fig4.savefig('biodiv_eps_'+name+'.png')
    plt.close()
    
def C_print(Cs, S_mean_1N, S_dev_1N, S_mean_2N, S_dev_2N, 
              S_mean_1R, S_dev_1R, S_mean_2R, S_dev_2R, 
              name, dir_name, S1, S2, eps):
    import matplotlib.pyplot as plt
    import math
    #vecchia variabile: eps_S
    #N/R_eps_S = (eps, S_mean_1, S_dev_1, S_mean_2, S_dev_2 )
  
    
    fig, (aa,bb) = plt.subplots(2,2, figsize = (9,8))
    ax1 = aa[0]
    ax2 = aa[1] 
    ax3 = bb[0]
    ax4 = bb[1]
    #[ax1, ax2, ax3, ax4]
    ax1.plot(Cs, S_mean_1N, '.')
    ax1.errorbar(Cs, S_mean_1N, yerr = S_dev_1N, fmt = 'b.')
    ax1.set_title('S(C) nested con eps = {}'.format(eps))
    ax1.set_ylabel('S1 all\'equilibrio con S1 iniziale = {}'.format(S1) )
    ax1.set_xlabel('connettanza C') 
    ax1.grid()
    ax1.set_ylim(0)
    ax1.set_autoscale_on(True)
    
    ax3.plot(Cs,S_mean_2N, '.')
    ax3.errorbar(Cs, S_mean_2N, yerr = S_dev_2N, fmt = 'b.')
    ax3.set_ylabel('S2 all\'equilibrio con S2 iniziale = {}'.format(S2) )
    ax3.set_xlabel('connettanza C') 
    ax3.grid() 
    ax3.set_ylim(0)
    ax3.set_autoscale_on(True)
    
    ax2.plot(Cs, S_mean_1R, '.')
    ax2.errorbar(Cs, S_mean_1R, yerr = S_dev_1R, fmt = 'b.')
    ax2.set_title('S(C) casuale con eps = {}'.format(eps))
    ax2.set_ylabel('S1 all\'equilibrio con S1 iniziale = {}'.format(S1))
    ax2.set_xlabel('connettanza C') 
    ax2.grid()
    ax2.set_ylim(0)
    ax2.set_autoscale_on(True)
    
    ax4.plot(Cs,S_mean_2R, '.')
    ax4.errorbar(Cs, S_mean_2R, yerr = S_dev_2R, fmt = 'b.')
    ax4.set_ylabel('S2 all\'equilibrio con S2 iniziale = {}'.format(S2))
    ax4.set_xlabel('connettanza C') 
    ax4.grid() 
    ax4.set_ylim(0)
    ax4.set_autoscale_on(True)
    
    import os
    path = dir_name
    os.chdir(path)
    fig.savefig('S_C_'+name+'.png')
    plt.close()
    
    d_S1 = []
    d_S2 = []
    s_S1 = []
    s_S2 = []
    for i in range(len(S_mean_1N)):
        delta1 = (S_mean_1N[i] - S_mean_1R[i])/S1
        s_q1 = math.pow(S_dev_1N[i]/S1,2) + math.pow(S_dev_1R[i]/S1, 2)
        sigma1 = math.sqrt(s_q1)
        d_S1.append(delta1)
        s_S1.append(sigma1)
        
    for i in range(len(S_mean_2N)):
        delta2 = (S_mean_2N[i] - S_mean_2R[i])/S2
        s_q2 = math.pow(S_dev_2N[i]/S2,2) + math.pow(S_dev_2R[i]/S2, 2)
        sigma2 = math.sqrt(s_q2)
        d_S2.append(delta2)
        s_S2.append(sigma2)

    fig2, [ax5,ax6] = plt.subplots(2,1, figsize = (6,6))
    
    ax5.plot(Cs, d_S1, '.')
    ax5.errorbar(Cs, d_S1, yerr = s_S1, fmt = 'b.')
    ax5.set_title('deltaS stazionaria su S iniziale al variare di C per eps = {} '.format(eps))
    ax5.set_ylabel('(S1 nest - S1 rand)/S1 con S1 = {}'.format(S1))
    ax5.set_xlabel('connettanza C')
    ax5.grid()
    ax5.set_autoscale_on(True)
    
    ax6.plot(Cs, d_S2, '.')
    ax6.errorbar(Cs, d_S2, yerr = s_S2, fmt = 'b.')
    ax6.set_ylabel('(S2 nest - S2 rand)/S2 con S2 = {}'.format(S2))
    ax6.set_xlabel('connettanza C')
    ax6.grid()
    ax6.set_autoscale_on(True)
    
    fig2.savefig('deltaS_C_'+name+'.png')
    plt.close()
    
def print_C_zoom(B_Ns, sB_Ns, B_Rs, sB_Rs, deltas, sigmas):
    import matplotlib.pyplot as plt  
    #NOTE: 'seaborn' is not the original style that you find in matplotlib!
    #create a style in a more flexible way -> seaborn was modified by myself
    plt.style.use('seaborn')
    #print('deltas = ', deltas)
    #print('sigmas = ', sigmas)
    Cs = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]
    S1 = 10
    S2 = 10
    eps = 0.1
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(Cs, B_Ns[0], 'r.', label = 'nested I tipo')
    ax.errorbar(Cs, B_Ns[0], yerr = sB_Ns[0], fmt = 'r.')
    
    ax.plot(Cs, B_Ns[1], 'b.', label = 'nested II tipo')
    ax.errorbar(Cs, B_Ns[1], yerr = sB_Ns[1], fmt = 'b.')
    
    ax.plot(Cs, B_Rs[0], 'g.', label = 'random: <C> = C')
    ax.errorbar(Cs, B_Rs[0], yerr = sB_Rs[0], fmt = 'g.')
    
    ax.plot(Cs, B_Rs[1], 'm.', label = 'random C = cost')
    ax.errorbar(Cs, B_Rs[1], yerr = sB_Rs[1], fmt = 'm.')
    
    #ax.grid()
    ax.set_title('Biodiversità in funzione di C  per '+u"\u03B5"+' = {}'.format(eps))
    ax.set_xlabel('Connettanza C')
    ax.set_ylabel(r'$S_1 + S_2$'+' con '+r'$ S_0 = {}$'.format(S1+S2))
    ax.set_xlim(left = 0)
    ax.set_ylim(bottom = 0)
    ax.legend(loc = 'lower right', fontsize = 'large')
    plt.tight_layout()
    
    import os
    #this was just an exception, it has to be revised
    path = 'C:/Users/Utente/Anaconda3/Cooperazione/100-100'
    os.chdir(path)
    fig.savefig('4S_C-'+repr(eps)+'-v3.png')
    plt.close()
    
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.plot(Cs, deltas[0], 'r.', label = 'nested I tipo vs random')
    ax2.errorbar(Cs, deltas[0], yerr = sigmas[0], fmt = 'r.')
    #r'$[log(T_{ass})]$'
    #u"\u0394"
    ax2.plot(Cs, deltas[1], 'b.', label = 'nested II tipo vs random')
    ax2.errorbar(Cs, deltas[1], yerr = sigmas[1], fmt = 'b.')
    #ax2.grid()
    ax2.set_title(u"\u0394"+r'$S/S_0$'+' in funzione di C per '+u"\u03B5"+' = {}'.format(eps))
    ax2.set_xlabel('Connettanza C')
    ax2.set_ylabel(u"\u0394"+r'$S/S_0$'+' con '+r'$S_0 = {}$'.format(S1+S2))
    ax2.set_xlim(left = 0)
    #ax.set_ylim(bottom = 0)
    ax2.legend(fontsize = 'large')
    plt.tight_layout()
    fig2.savefig('2deltaS_C-'+repr(eps)+'-v3.png')
    plt.close()
    
def NODF_print(S1_m, S1_d, S2_m, S2_d, eps, C, NODFs, S1, S2, rip, parent_dir):
    import matplotlib.pyplot as plt
    #NOTE: 'seaborn' is not the original style that you find in matplotlib!
    #create a style in a more flexible way -> seaborn was modified by myself
    plt.style.use('seaborn')
    #plt.style.use('ggplot')
    import math
    
    print('S1_m = ', S1_m)
    print('S2_m = ', S2_m)
    print('NODFs = ', NODFs)
    
    fig2, [ax5,ax6] = plt.subplots(1,2, figsize = (9,5))
    
    ax5.plot(NODFs,S1_m, '.')
    ax5.errorbar(NODFs, S1_m, yerr = S1_d, fmt = 'b.')
    #ax5.set_title('S1 al variare di NODF per (eps, C) = ({}, {} )'.format(eps,C))
    #ax5.set_ylabel('S1 all\'equilibrio con S1 iniziale = {}'.format(S1))
    ax5.set_title('S1(NODF) per ('+ u"\u03B5"+', C) = ({}, {} )'.format(eps,C))
    ax5.set_ylabel('Specie coesistenti S1 su {}'.format(S1))
    ax5.set_xlabel('Nestedness [NODF]')
    #ax5.grid()
    ax5.set_autoscale_on(True)
    ax5.set_ylim(0,S1)
    
    ax6.plot(NODFs, S2_m, '.')
    ax6.errorbar(NODFs, S2_m, yerr = S2_d, fmt = 'b.')
    #ax6.set_title('S2 al variare di NODF per (eps, C) = ({}, {} )'.format(eps,C))
    #ax6.set_ylabel('S2 all\'equilibrio con S2 iniziale = {}'.format(S2))
    ax6.set_title('S2(NODF) per ('+ u"\u03B5"+', C) = ({}, {} )'.format(eps,C))
    ax6.set_ylabel('Specie coesistenti S2 su {}'.format(S1))
    ax6.set_xlabel('Nestedness [NODF]')
    #ax6.grid()
    ax6.set_autoscale_on(True)
    ax6.set_ylim(0,S2)
    plt.tight_layout()
    import os
    path = parent_dir
    os.chdir(path)
    fig2.savefig('S12_NODF_'+eps+'-'+C+'-'+rip+'.png')
    plt.close()
    
    S = []
    d = []
    for i in range(len(S1_m)):
        somma = (S1_m[i] + S2_m[i])
        s_q2 = math.pow(S1_d[i],2) + math.pow(S2_d[i], 2)
        err = math.sqrt(s_q2)
        S.append(somma)
        d.append(err)
        
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(NODFs, S, '.', label = 'Dati per:\n '+ u"\u03B5"+' = {} \n C = {}'.format(eps,C))
    ax.errorbar(NODFs, S, yerr = d, fmt = 'b.')
    #ax.set_title('S al variare di NODF per (eps, C) = ({}, {} )'.format(eps,C))
    #ax.set_ylabel('S all\'equilibrio con S iniziale = {}'.format(S1+S2))
    #ax.set_title('S(NODF) per (eps, C) = ({}, {} )'.format(eps,C))
    ax.set_ylabel('Specie coesistenti S su {}'.format(S1+S2))
    ax.set_xlabel('Nestedness [NODF]')
    #ax.grid()
    ax.legend(fontsize = 'large')
    plt.tight_layout()
    fig.savefig('S_NODF_'+eps+'-'+C+'-'+rip+'.png')
    plt.close()
    
    deltas = []
    sigmas = []
    for i in range(len(S)):
        diff = (S[i] - S[-1])/(S1+S2)
        s_q2 = math.pow(d[i],2) + math.pow(d[-1], 2)
        err = math.sqrt(s_q2)/(S1+S2)
        deltas.append(diff)
        sigmas.append(err)
        
    fig1 = plt.figure()
    ax = fig1.add_subplot(111)
    #ax.plot(NODFs, deltas, '.')
    ax.plot(NODFs, deltas, '.', label = 'Dati per:\n '+ u"\u03B5"+' = {} \n C = {}'.format(eps,C))
    ax.errorbar(NODFs, deltas, yerr = sigmas, fmt = 'b.')
    #ax.set_title('deltaS/S al variare di NODF per (eps, C) = ({}, {} )'.format(eps,C))
    ax.set_ylabel(u"\u0394"+r'$S/S_0$'+' con '+r'$S_0 = {}$'.format(S1+S2))
    ax.set_xlabel('Nestedness [NODF]')
    #ax.grid()
    ax.legend(fontsize = 'large')
    plt.tight_layout()
    fig1.savefig('deltaS_NODF_'+eps+'-'+C+'-'+rip+'-v1.png')
    plt.close()
    
    print('deltas = ', deltas, '\n')
    print('sigmas = ', sigmas, '\n')
    
def e_hist(data):
    #import my_output as O
    #import math
    from analyser import n_analysis2
    eps_len = (len(data) - 5)
    epsilons = []
    
    parent_dir = data[0]
    print('parent_dir = ', parent_dir)
    N =  int(data[1])
    #S1 = int(math.sqrt(N))
    #S2 = int(math.sqrt(N))
    #rip = data[2]
    for j in range(eps_len):
        y = float(data[3+j])
        epsilons.append(y)
    
    p = data[-2]
    #devo riuscire a chiamare n analysis per n1, n2, N e R!
    v_N_n1_rips = n_analysis2('N_n1_', parent_dir)
    v_N_n2_rips = n_analysis2('N_n2_', parent_dir)
    v_R_n1_rips = n_analysis2('R_n1_', parent_dir)
    v_R_n2_rips = n_analysis2('R_n2_', parent_dir)
    plot_eps_hist(v_N_n1_rips, epsilons, p, N, ['N_', 'n1_'], parent_dir)
    plot_eps_hist(v_N_n2_rips, epsilons, p, N, ['N_', 'n2_'], parent_dir)
    plot_eps_hist(v_R_n1_rips, epsilons, p, N, ['R_', 'n1_'], parent_dir)
    plot_eps_hist(v_R_n2_rips, epsilons, p, N, ['R_', 'n2_'], parent_dir)
    
def plot_eps_hist(v_n_rips, epsilons, p, N, names, parent_dir):
    # names = ['N_','n1_'] o cose del genere
    for i in range(len(epsilons)):
        eps = epsilons[i]
        e_plot_hist(v_n_rips[i], eps, p, N, names, parent_dir+'/'+repr(eps)+'-'+p)

def e_plot_hist(v_n_rip, eps, p, N, names, dir_name):
    import matplotlib.pyplot as plt
    #import numpy as np
    b = int(N/5)
    rip = len(v_n_rip)
    #print('rip = ', rip, '\n')
    
    fig1 = plt.figure()
    ax0 = fig1.add_subplot(111)
    if names[1] == 'n1_':
        if names[0] == 'N_':
            ax0.set_title('Specie I gruppo nested con eps = {}'.format(eps))
        else:
            ax0.set_title('Specie I gruppo casuale con eps = {}'.format(eps))
    else:
        if names[0] == 'N_':
            ax0.set_title('Specie II gruppo nested con eps = {}'.format(eps))
        else:
            ax0.set_title('Specie II gruppo casuale con eps = {}'.format(eps))
    
    m = min([rip, 5])
    
    for i in range(m):
        ax0.hist(v_n_rip[i], bins = N-1, range = (1,N), density = True, 
                 cumulative = -1, histtype = 'step', label = 'realizzazione {}'.format(i+1))
    #ax0.setp(lines, linewidth = 4)
    ax0.legend(loc='upper right')
    ax0.set_xlabel('Numero individui n')
    ax0.set_ylabel('Probabilità cumulata P>(n)')
    import os
    path = dir_name
    os.chdir(path)
    fig1.savefig(names[0]+names[1]+repr(eps)+'-'+p+"_hist.png")
    plt.close()
        
    fig2 = plt.figure()
    ax = fig2.add_subplot(111)
    v_n_tot = []
    for i in range(rip):
        v_n_tot = v_n_tot + v_n_rip[i]
        
    if len(v_n_tot) != len(v_n_rip[0])*rip:
        print('Attenzione, len(v_n_tot) = ', len(v_n_tot), '\n' )
        
    ax.hist(v_n_tot, bins = N-1, range = (1,N), density = True, 
                 cumulative = -1,  histtype = 'stepfilled', label = 'P cumulata complessiva'.format(i+1))
    
    if names[1] == 'n1_':
        if names[0] == 'N_':
            ax.set_title('Specie I gruppo nested per {} realizzazioni  con eps = {}'.format(rip,eps))
        else:
            ax.set_title('Specie I gruppo casuale per {} realizzazioni  con eps = {}'.format(rip,eps))
    else:
        if names[0] == 'N_':
            ax.set_title('Specie II gruppo nested per {} realizzazioni  con eps = {}'.format(rip,eps))
        else:
            ax.set_title('Specie II gruppo casuale per {} realizzazioni  con eps = {}'.format(rip,eps))
    ax.legend(loc='upper right')
    ax.set_xlabel('Numero individui n')
    ax.set_ylabel('Probabilità cumulata P>(n)')
    
    
    fig2.savefig(names[0]+names[1]+repr(eps)+'-'+p+"_hist2.png")
    plt.close()
 
def p_hist(data):
    #import my_output as O
    #import math
    from analyser import n_analysis2
    ps_len = (len(data) - 5)
    ps = []
    
    parent_dir = data[0]
    N =  int(data[1])
    #S1 = int(math.sqrt(N))
    #S2 = int(math.sqrt(N))
    #rip = data[2]
    eps =  data[3]
    for j in range(ps_len):
        y = float(data[4+j])
        ps.append(y)  
    #devo riuscire a chiamare n analysis per n1, n2, N e R!
    v_N_n1_rips = n_analysis2('N_n1_', parent_dir)
    v_N_n2_rips = n_analysis2('N_n2_', parent_dir)
    v_R_n1_rips = n_analysis2('R_n1_', parent_dir)
    v_R_n2_rips = n_analysis2('R_n2_', parent_dir)
    plot_ps_hist(v_N_n1_rips, eps, ps, N, ['N_', 'n1_'], parent_dir)
    plot_ps_hist(v_N_n2_rips, eps, ps, N, ['N_', 'n2_'], parent_dir)
    plot_ps_hist(v_R_n1_rips, eps, ps, N, ['R_', 'n1_'], parent_dir)
    plot_ps_hist(v_R_n2_rips, eps, ps, N, ['R_', 'n2_'], parent_dir)
    
def plot_ps_hist(v_n_rips, eps, ps, N, names, parent_dir):
    # names = ['N_','n1_'] o cose del genere
    for i in range(len(ps)):
        p = ps[i]
        p_plot_hist(v_n_rips[i], eps, p, N, names, parent_dir+'/'+eps+'-'+repr(p))
    
def p_plot_hist(v_n_rip, eps, C, N, names, dir_name):
    import matplotlib.pyplot as plt
    #import numpy as np
    b = int(N/5)
    rip = len(v_n_rip)
    #print('rip = ', rip, '\n')
    
    fig1 = plt.figure()
    ax0 = fig1.add_subplot(111)
    if names[1] == 'n1':
        if names[0] == 'N_':
            ax0.set_title('Specie I gruppo nested con C = {}'.format(C))
        else:
            ax0.set_title('Specie I gruppo casuale con C = {}'.format(C))
    else:
        if names[0] == 'N_':
            ax0.set_title('Specie II gruppo nested con C = {}'.format(C))
        else:
            ax0.set_title('Specie II gruppo casuale con C = {}'.format(C))
    
    m = min([rip, 5])
    
    for i in range(m):
        ax0.hist(v_n_rip[i], bins = N-1, range = (1,N), density = True, 
                 cumulative = -1, histtype = 'step', label = 'realizzazione {}'.format(i+1))
    #ax0.setp(lines, linewidth = 4)
    ax0.legend(loc='upper right')
    ax0.set_xlabel('Numero individui n')
    ax0.set_ylabel('Probabilità cumulata P>(n)')
    import os
    path = dir_name
    os.chdir(path)
    fig1.savefig(names[0]+names[1]+eps+'-'+repr(C)+"_hist.png")
    plt.close()
        
    fig2 = plt.figure()
    ax = fig2.add_subplot(111)
    v_n_tot = []
    for i in range(rip):
        v_n_tot = v_n_tot + v_n_rip[i]
        
    if len(v_n_tot) != len(v_n_rip[0])*rip:
        print('Attenzione, len(v_n_tot) = ', len(v_n_tot), '\n' )
        
    ax.hist(v_n_tot, bins = N-1, range = (1,N), density = True, 
                 cumulative = -1, label = 'P cumulata complessiva'.format(i+1))
    
    if names[1] == 'n1':
        if names[0] == 'N_':
            ax.set_title('Specie I gruppo nested per {} realizzazioni con C = {}'.format(rip,C))
        else:
            ax.set_title('Specie I gruppo casuale per {} realizzazioni con C = {}'.format(rip,C))
    else:
        if names[0] == 'N_':
            ax.set_title('Specie II gruppo nested per {} realizzazionicon C = {}'.format(rip,C))
        else:
            ax.set_title('Specie II gruppo casuale per {} realizzazioni con C = {}'.format(rip,C))
    ax.legend(loc='upper right')
    ax.set_xlabel('Numero individui n')
    ax.set_ylabel('Probabilità cumulata P>(n) ')
    
    
    fig2.savefig(names[0]+names[1]+eps+'-'+repr(C)+"_hist2.png")
    plt.close()  
    
def S_plot(S, eps, C, name, dir_name):
    import matplotlib.pyplot as plt
    tau_max = len(S)
    tau = [x for x in range(tau_max)]    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(tau, S)
    
    if name == 'N_S1_':
        ax.set_title('S1(tau) nested per eps = {} e C = {}'.format(eps,C))
        ax.set_ylabel('S1 con specie iniziali = {}'.format(S[0]))
    elif name == 'N_S2_':
        ax.set_title('S2(tau) nested per eps = {} e C = {}'.format(eps,C))
        ax.set_ylabel('S2 con specie iniziali = {}'.format(S[0]))
    elif name == 'R_S1_': 
        ax.set_title('S1(tau) casuali per eps = {} e C = {}'.format(eps,C))
        ax.set_ylabel('S1 con specie iniziali = {}'.format(S[0]))
    else:
        ax.set_title('S2(tau) casuali per eps = {} e C = {}'.format(eps,C))
        ax.set_ylabel('S2 con specie iniziali = {}'.format(S[0]))
    
    ax.set_xlabel('Tempo tau [step/N]')
    ax.grid()
    ax.set_xlim(left = 0)
    ax.set_ylim(0, S[0]+1)
    import os
    path = dir_name
    os.chdir(path)
    fig.savefig(name+'-'+repr(eps)+'-'+repr(C)+'-S_plot.png')

    plt.close()

def S_plot2(S, eps, C, NODF, name, dir_name):
    import matplotlib.pyplot as plt
    tau_max = len(S)
    tau = [x for x in range(tau_max)]    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(tau, S)
    
    if name == 'S1_':
        ax.set_title('S1(tau) per eps = {}, C = {} e NODF = {}'.format(eps,C, NODF))
        ax.set_ylabel('S1 con specie iniziali = {}'.format(S[0]))
    elif name == 'S2_':
        ax.set_title('S2(tau) per eps = {}, C = {} e NODF = {}'.format(eps,C, NODF))
        ax.set_ylabel('S2 con specie iniziali = {}'.format(S[0]))
    ax.set_xlabel('Tempo tau [step/N]')
    ax.grid()
    ax.set_xlim(left = 0)
    ax.set_ylim(0, S[0]+1)
    import os
    path = dir_name
    os.chdir(path)
    fig.savefig(name+'-'+repr(eps)+'-'+repr(C)+'-'+repr(NODF)+'-S_plot.png')

    plt.close()
    
def print_NODF_step(NODFs, C, P, dir_name):
    import matplotlib.pyplot as plt
    #NOTE: 'seaborn' is not the original style that you find in matplotlib!
    #create a style in a more flexible way -> seaborn was modified by myself
    plt.style.use('seaborn')
    step = [x for x in range(len(NODFs))]
    print('NODFs = ', NODFs)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(step, NODFs, label = 'C = 0.35')
    #ax.set_title('NODF per {} step da nested a random con C = {}'.format(step[-1],C))
    ax.set_xlabel('Numero di steps da {} scambi casuali ciascuno'.format(P))
    ax.set_ylabel('Nestedness [NODF]')
    ax.legend(fontsize = 'large')
    plt.tight_layout()
    import os
    path = dir_name
    os.chdir(path)
    fig.savefig('NODF_step-'+repr(C)+'-'+repr(P)+'.png')

    plt.close()
    
def print_NODF_step2(NODFs, C, P, dir_name):
    import matplotlib.pyplot as plt
    step = [x for x in range(len(NODFs))]
    print('NODFs = ', NODFs)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(step, NODFs, 'o')
    ax.set_title('NODF scelte da nested a random con C = {}'.format(C))
    ax.set_xlabel('Ordine matrici scelte')
    ax.set_ylabel('Nestedness [NODF]')
    import os
    path = dir_name
    os.chdir(path)
    fig.savefig('NODF_selezione-'+repr(C)+'-'+repr(P)+'.png')
    
    plt.close()