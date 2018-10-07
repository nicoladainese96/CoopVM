def print_tuple (K, name, dir_name, d=2, rnd =2):
    """Stampa una lista di tuple fatti di d numeri.
    Di default d=2, cioè tratta coppie, e quindi è
    una generalizzazione di print_tuple1.
    Accetta una lista di tuple. Non ritorna nulla.
    """
    
    from ensure_dir import ensure_dir
    file_path = dir_name+'//data_plot//'+ name + '.txt'
    ensure_dir(file_path)
    with open(file_path, 'a') as fS:
    #with open("stat_" + name + ".txt", "w") as fS:
         
        for i in range(0,d-1):
            print("{}    ".format(round(K[i],rnd)), end ='', file = fS)
        print("{}".format(round(K[d-1],rnd)), file = fS)

def print_tuple1 (K, name, dir_name, d=2, rnd = 2):
    """Stampa una lista di tuple fatti di d numeri.
    Di default d=2, cioè tratta coppie, e quindi è
    una generalizzazione di print_tuple1.
    Accetta una lista di tuple. Non ritorna nulla.
    """
    #import os
    from ensure_dir import ensure_dir
    #attenzione qui ho aggiunto //data_plot
    file_path = dir_name+'//data_plot//'+ name + ".txt"
    ensure_dir(file_path)
    with open(file_path, 'a') as fS:
    #with open("stat_" + name + ".txt", "w") as fS:
        if fS.seek(0,2) == 0:
            for i in range(len(K)):
                for j in range(0,d-1):
                    print("{}    ".format(round(K[i][j],rnd)), end ='', file = fS)
                print("{}".format(round(K[i][d-1],2)), file = fS)
                
def print_tuple2 (K, name, dir_name, d=2, rnd = 2):
    """Stampa una lista di tuple fatti di d numeri.
    Di default d=2, cioè tratta coppie, e quindi è
    una generalizzazione di print_tuple1.
    Accetta una lista di tuple. Non ritorna nulla.
    """
    #import os
    from ensure_dir import ensure_dir
    #attenzione qui ho aggiunto //data_plot
    file_path = dir_name+'//data_plot//'+ name + ".txt"
    ensure_dir(file_path)
    with open(file_path, 'a') as fS:
    #with open("stat_" + name + ".txt", "w") as fS:
        if fS.seek(0,2) == 0:
            for i in range(len(K)):
                for j in range(0,d-1):
                    print("{}    ".format(round(K[i][j],rnd)), end ='', file = fS)
                print("{}".format(round(K[i][d-1],2)), file = fS)

def print_tuple3 (K, name, dir_name, d=2):
    """Stampa una lista di tuple fatti di d numeri.
    Di default d=2, cioè tratta coppie, e quindi è
    una generalizzazione di print_tuple1.
    Accetta una lista di tuple. Non ritorna nulla.
    """
    #import os
    from ensure_dir import ensure_dir
    file_path = dir_name+"\\data_plot\\"+ name + ".txt"
    ensure_dir(file_path)
    with open(file_path, 'w') as fS:
    #with open("stat_" + name + ".txt", "w") as fS:
         
         for x in K:
            for i in range(0,d-1):
                print("{}    ".format(x[i]), end ='', file = fS)
            print("{}".format(x[d-1]), file = fS)
            
def tab_reader (name, dir_name, d = 2):
    #import os
    from ensure_dir import ensure_dir
    #file_path = "C:\Users\Utente\Anaconda3\Cooperazione\\"+dir_name+"\\data_plot\\"+ name + ".txt"
    file_path = dir_name+"//data_plot//"+ name + ".txt"
    ensure_dir(file_path)
    with open (file_path, 'r') as f:
        l = []
        l2 = []
        T = 0
        while T == 0:
            s = f.readline().split('    ')
            if s[0] != '':
                d = len(s)
                l2 = []
                for i in range(1,d-1):
                    l2.append(int(s[i]))
                z = s[d-1].split('\n')
                l2.append(int(z[0]))
                l.append((int(s[0]),l2))
            else:
                T = 1
                break
    return l

def tab_reader2 (name, dir_name):
    from ensure_dir import ensure_dir
    file_path = dir_name+"//data_plot//"+ name + ".txt"
    ensure_dir(file_path)
    with open (file_path, 'r') as f:
        l = []
        l2 = []
        T = 0
        while T == 0:
            s = f.readline().split('    ')
            if s[0] != '':
                d = len(s)
                l2 = []
                for i in range(0,d-1):
                    l2.append(int(s[i]))
                z = s[d-1].split('\n')
                l2.append(int(z[0]))
                l.append(l2)
            else:
                T = 1
                break
    return l



def old_tab_reader2 (name, dir_name, d = 2):
    #import os
    from ensure_dir import ensure_dir
    #file_path = "C:\Users\Utente\Anaconda3\Cooperazione\\"+dir_name+"\\data_plot\\"+ name + ".txt"
    file_path = "C:/Users/Utente/Anaconda3/Cooperazione//"+dir_name+"//data_plot//"+ name + ".txt"
    ensure_dir(file_path)
    with open (file_path, 'r') as f:
        l = []
        l2 = []
        T = 0
        while T == 0:
            s = f.readline().split('    ')
            if s[0] != '':
                d = len(s)
                l2 = []
                for i in range(1,d-1):
                    l2.append(int(s[i]))
                z = s[d-1].split('\n')
                l2.append(int(z[0]))
                l.append((int(s[0]),l2))
            else:
                T = 1
                break
    return l

def my_pyplot(name1, name2, dir_name, info, d=2):
    from ensure_dir import ensure_dir
    #file_path = "C:\Users\Utente\Anaconda3\Cooperazione\\"+dir_name+"\\data_plot\\"+ name + ".txt"
    file_path1 = dir_name+"//data_plot//"+ name1 + ".txt"
    ensure_dir(file_path1)
    with open (file_path1, 'r') as f:
        l1 = []
        for i in range(d):
            l1.append([])
        T = 0
        while T == 0:
            s = f.readline().split('    ')
            if s[0] != '':
                b = len(s)
                l1[0].append(int(s[0]))
                
                for j in range(1,b-1):
                    l1[j].append(int(s[j]))
                    
                z = s[b-1].split('\n')
                l1[b-1].append(int(z[0]))
            else:
                T = 1
                break
    file_path2 = dir_name+"//data_plot//"+ name2 + ".txt"
    ensure_dir(file_path2)
    with open (file_path2, 'r') as f:
        l2 = []
        for i in range(d):
            l2.append([])
        T = 0
        while T == 0:
            s = f.readline().split('    ')
            if s[0] != '':
                b = len(s)
                l2[0].append(int(s[0]))
                
                for j in range(1,b-1):
                    l2[j].append(int(s[j]))
                    
                z = s[b-1].split('\n')
                l2[b-1].append(int(z[0]))
            else:
                T = 1
                break
                    
    
    import matplotlib.pyplot as plt
    plt.style.use('seaborn')
    #fig, [ax1,ax2] = plt.subplots(1,2, figsize = (9,4))
    fig, [ax1,ax2] = plt.subplots(2,1,figsize = (4,8))
    #fig, [ax1,ax2] = plt.subplots(2,1)
    ax1.plot(l1[0], l1[1], 'r.')
    ax1.set(ylabel= info['ylab1'], title = info['tit1'])
    ax1.grid()
    ax1.set_ylim(0)
    ax1.set_autoscale_on(True)
    
    ax2.plot(l2[0], l2[1], 'r.')
    ax2.set(xlabel = info['xlab'] , ylabel= info['ylab2'], title = info['tit2'])
    ax2.grid()
    ax2.set_ylim(0)
    ax2.set_autoscale_on(True)
    plt.tight_layout()
    
    import os
    path = dir_name
    
    os.chdir(path)
    fig.savefig(name1+"_plot.png")
    plt.close()
    
def plot_hist(l1, l2, s_1, s_2, name, dir_name, info):
    import matplotlib.pyplot as plt
    
    m1 = l1[:]
    N1 = len(l1)
    m1.reverse()
    n_bins1 = 0
    for i in range(len(m1)):
        if m1[i] == 0:
            continue
        else:
            n_bins1 = N1 - i
            break
    x1 = [x+1 for x in range(n_bins1)]
    w1 = l1[:n_bins1]
    s1 = s_1[:n_bins1]
             
    m2 = l2[:]
    N2 = len(l2)
    m2.reverse()
    n_bins2 = 0
    for i in range(len(m2)):
        if m2[i] == 0:
            continue
        else:
            n_bins2 = N2 - i
            break
    x2 = [x+1 for x in range(n_bins2)]
    w2 = l2[:n_bins2]
    s2 = s_2[:n_bins2]
        
        
    fig, [ax1, ax2] = plt.subplots(1,2, figsize = (9,5))
    
    
    # the histogram of the data
    #n1, bins1, patches1 = ax1.hist(x1, bins = n_bins1, range = (0.5, n_bins1+0.5), density = True, weights = w1)
    n1, bins1, patches1 = ax1.hist(x1, bins = n_bins1, range = (0.5, n_bins1+0.5), weights = w1)
    #n2, bins2, patches2 = ax2.hist(x2, bins = n_bins2, range = (0.5, n_bins2+0.5), density = True, weights = w2)
    #print('n1 = ', n1)
    n2, bins2, patches2 = ax2.hist(x2, bins = n_bins2, range = (0.5, n_bins2+0.5), weights = w2)
    #print('bins1 = ', bins1)
    
    #ax1.errorbar(x1, w1, yerr = s1, fmt = 'r.')
    #ax1.set_xlabel(info['xlab'])
    ax1.set_ylabel(info['ylab_1'])
    ax1.set_title(info['tit1'])
    ax1.grid()
    ax1.set_autoscale_on(True)
    ax1.set_xlim(1)
    
    #ax2.errorbar(x2, w2, yerr = s2, fmt = 'r.')
    ax2.set_xlabel(info['xlab'])
    ax2.set_ylabel(info['ylab_2'])
    ax2.set_title(info['tit2'])
    ax2.grid()
    ax2.set_autoscale_on(True)
    ax2.set_xlim(1)
    
    import os
    path = dir_name
    os.chdir(path)
    fig.savefig(name+"_hist.png")
    plt.close()

def eps_print(R_eps_S, N_eps_S, name, dir_name, info1, info2, S1, S2):
    import matplotlib.pyplot as plt
    import math
    #vecchia variabile: eps_S
    #N/R_eps_S = (eps, S_mean_1, S_dev_1, S_mean_2, S_dev_2 )
    epsN = []
    S_mean_1N = []
    S_dev_1N = []
    S_mean_2N = []
    S_dev_2N = []
    N_data = (epsN,S_mean_1N, S_dev_1N, S_mean_2N, S_dev_2N)
    for i in range(len(N_eps_S)):
        for k in range(len(N_eps_S[0])):
            N_data[k].append(N_eps_S[i][k])
            
    epsR = []
    S_mean_1R = []
    S_dev_1R = []
    S_mean_2R = []
    S_dev_2R = []
    R_data = (epsR,S_mean_1R, S_dev_1R, S_mean_2R, S_dev_2R)
    for i in range(len(R_eps_S)):
        for k in range(len(R_eps_S[0])):
            R_data[k].append(R_eps_S[i][k])
    
    
    fig, (aa,bb) = plt.subplots(2,2, figsize = (9,8))
    ax1 = aa[0]
    ax2 = aa[1] 
    ax3 = bb[0]
    ax4 = bb[1]
    #[ax1, ax2, ax3, ax4]
    ax1.plot(epsN, S_mean_1N, '.')
    ax1.errorbar(epsN, S_mean_1N, yerr = S_dev_1N, fmt = 'b.')
    ax1.set_title(info1['tit1'])
    ax1.set_ylabel(info1['ylab_1'])
    ax1.set_xlabel(info1['xlab']) 
    ax1.grid()
    ax1.set_ylim(0)
    ax1.set_autoscale_on(True)
    
    ax3.plot(epsN,S_mean_2N, '.')
    ax3.errorbar(epsN, S_mean_2N, yerr = S_dev_2N, fmt = 'b.')
    ax3.set_ylabel(info1['ylab_2'])
    ax3.set_xlabel(info1['xlab']) 
    ax3.grid() 
    ax3.set_ylim(0)
    ax3.set_autoscale_on(True)
    
    ax2.plot(epsR, S_mean_1R, '.')
    ax2.errorbar(epsR, S_mean_1R, yerr = S_dev_1R, fmt = 'b.')
    ax2.set_title(info1['tit2'])
    ax2.set_ylabel(info1['ylab_1'])
    ax2.set_xlabel(info1['xlab']) 
    ax2.grid()
    ax2.set_ylim(0)
    ax2.set_autoscale_on(True)
    
    ax4.plot(epsR,S_mean_2R, '.')
    ax4.errorbar(epsR, S_mean_2R, yerr = S_dev_2R, fmt = 'b.')
    ax4.set_ylabel(info1['ylab_2'])
    ax4.set_xlabel(info1['xlab']) 
    ax4.grid() 
    ax4.set_ylim(0)
    ax4.set_autoscale_on(True)
    
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
    
    ax5.plot(epsN, d_S1, '.')
    ax5.errorbar(epsN, d_S1, yerr = s_S1, fmt = 'b.')
    ax5.set_title(info2['tit'])
    ax5.set_ylabel(info2['ylab_3'])
    ax5.set_xlabel(info1['xlab'])
    ax5.grid()
    ax5.set_autoscale_on(True)
    
    ax6.plot(epsN, d_S2, '.')
    ax6.errorbar(epsN, d_S2, yerr = s_S2, fmt = 'b.')
    ax6.set_ylabel(info2['ylab_4'])
    ax6.set_xlabel(info1['xlab'])
    ax6.grid()
    ax6.set_autoscale_on(True)
    
    fig2.savefig('deltaS_eps_'+name+'.png')
    plt.close()
    
def overview(N1, step, rip, t_tot, dir_name):
    from ensure_dir import ensure_dir
    file_path = dir_name+'//''overview1.txt'
    ensure_dir(file_path)
    with open(file_path, 'w') as f:
        print('N1 = ', N1, file=f)
        print('Numero step compiuti = ', step, file = f)
        print('Numero di realizzazioni = ', rip, file = f)
        print('Tau max = ', int(step/N1), file = f)
        print('Tempo totale impiegato per la simulazione = ', t_tot, 'min', file = f)
        
    file_path2 = 'C:/Users/Utente/Anaconda3/Cooperazione//overview.txt'
    ensure_dir(file_path2)
    with open(file_path2, 'a') as f:
        if f.seek(0,2) == 0:
            print('#N1:    Step:    Rip:    Tau:    t_tot', file = f)
        print(N1, step, int(step/N1), rip, t_tot, sep =  '    ', file=f)
        
def overview2(N1, S1, eps, p, rip, t_tot, dir_name):
    from ensure_dir import ensure_dir
    file_path = 'C:/Users/Utente/Anaconda3/Cooperazione//'+dir_name+'//''overview2.txt'
    ensure_dir(file_path)
    with open(file_path, 'w') as f:
        if f.seek(0,2) == 0:
            print('#N1:   S1:   eps:   p:   rip:  t_tot:', file = f)
        print(N1, S1, eps, p, rip, t_tot, sep =  '    ', file=f)
        
    file_path2 = 'C:/Users/Utente/Anaconda3/Cooperazione//overview2.txt'
    ensure_dir(file_path2)
    with open(file_path2, 'a') as f:
        if f.seek(0,2) == 0:
            print('#N1:   S1:   eps:   p:   rip:   t_tot:', file = f)
        print(N1, S1, eps, p, rip, t_tot, sep =  '    ', file=f)
        
def n_plot (dir_name, p_value, eps_values, N_info, R_info):
    RoN_plot('R', p_value, eps_values, dir_name+'//R-'+p_value, R_info)
    RoN_plot('N', p_value, eps_values, dir_name+'//N-'+p_value, N_info)
    
    
    
    
    
def RoN_plot (RoN, p_value, eps_values, dir_name, info):
    #devo leggere 10 file, farmi i vettori e poi plottarli
    for i in range(0,len(eps_values)):
        if eps_values[i] != 0:
            name1 = 'n1_'+RoN+'-'+p_value+'-'+repr(eps_values[i])+'-1'
            name2 = 'n2_'+RoN+'-'+p_value+'-'+repr(eps_values[i])+'-1'
        else:
            name1 = 'n1_'+RoN+'-'+p_value+'-'+format(eps_values[i],'.1f')+'-1'
            name2 = 'n2_'+RoN+'-'+p_value+'-'+format(eps_values[i],'.1f')+'-1'
        n1 = tab_reader2 (name1, dir_name)
        
        
        n2 = tab_reader2 (name2, dir_name)
        name = RoN+'-'+p_value+'-'+repr(eps_values[i])+'-1'
        multi_plot(n1, n2, name, dir_name, info, repr(eps_values[i]) )
        # 'specie I gruppo con eps = '
        #multi_plot(n2, name2, dir_name, info, repr(eps_values[i]))
   

def multi_plot(n1, n2, name, dir_name, info, eps):
    import matplotlib.pyplot as plt
    plt.style.use('seaborn')
    #u"\u03C4" tau
    #u"\u03B5" eps
    tau = [x for x in range(len(n1))]
    
    tau1_2 = []
    n1_2 = []
    for i in range(int(len(n1)/10)):
        tau1_2.append(tau[i*10])
        n1_2.append(n1[i*10])
    if len(tau1_2) != len(n1_2):
        print('len(tau1_2) = ', len(tau1_2))
        print('len(n1_2) = ',len(n1_2) )
    tau2_2 = []
    n2_2 = []
    for i in range(int(len(n2)/10)):
        tau2_2.append(tau[i*10])
        n2_2.append(n2[i*10])
    if len(tau2_2) != len(n2_2):
        print('len(tau2_2) = ', len(tau2_2))
        print('len(n2_2) = ',len(n2_2) )
        
    fig, [ax1,ax2] = plt.subplots(2,1,figsize = (8,8))
    ax1.plot(tau1_2, n1_2)
    #ax1.set_xlabel('Tempo '+u"\u03C4"+' [step/N1]')
    ax1.set_ylabel('Abbondanze n delle S1 specie')
    ax1.set_title(info['tit'] + 'specie I gruppo con '+u"\u03B5"+' = ' + eps)
    #ax1.grid()
    ax1.set_autoscale_on(True)
    
    ax2.plot(tau2_2, n2_2)
    ax2.set_xlabel('Tempo '+u"\u03C4"+' [step/N1]')
    ax2.set_ylabel('Abbondanze n delle S2 specie')
    ax2.set_title(info['tit'] + 'specie II gruppo con '+u"\u03B5"+' = ' + eps)
    #ax2.grid()
    ax2.set_autoscale_on(True)
    
    plt.tight_layout()
    import os
    path = dir_name
    os.chdir(path)
    fig.savefig(name+'_plots.png')
    plt.close()
    
    
    
def print_deg_x(N_deg_x1, N_deg_x2, R_deg_x1, R_deg_x2, name, dir_name, info1, S1, S2):
    import matplotlib.pyplot as plt
    
    fig, (aa,bb) = plt.subplots(2,2, figsize = (10,8))
    ax1 = aa[0]
    ax2 = aa[1] 
    ax3 = bb[0]
    ax4 = bb[1]
    XM11 = max(N_deg_x1[1])
    ax1.plot(N_deg_x1[0], N_deg_x1[1], '.')
    ax1.errorbar(N_deg_x1[0], N_deg_x1[1], yerr = N_deg_x1[2], fmt = 'b.')
    #ax1.set_title(info1['tit1'])
    ax1.set_ylabel(info1['ylab_1'])
    ax1.set_xlabel(info1['xlab_1']) 
    ax1.set_title('Nested con S1 = {} e S2 = {}'.format(S1,S2))
    ax1.grid()
    ax1.set_xlim(0,S1+1)
    if XM11 < 0.4:
        ax1.set_ylim(-0.1, 0.5)
    else:
        ax1.set_ylim(-0.1, XM11 + 0.1)
    ax1.set_autoscale_on(True)
    
    XM21 = max(N_deg_x2[1])
    ax3.plot(N_deg_x2[0], N_deg_x2[1], '.')
    ax3.errorbar(N_deg_x2[0], N_deg_x2[1], yerr = N_deg_x2[2], fmt = 'b.')
    ax3.set_ylabel(info1['ylab_2'])
    ax3.set_xlabel(info1['xlab_2']) 
    ax3.grid() 
    ax3.set_xlim(0,S2+1)
    if XM21 < 0.4:
        ax3.set_ylim(-0.1, 0.5)
    else:
        ax3.set_ylim(-0.1, XM21 + 0.1)
    ax3.set_autoscale_on(True)
    
    XM12 = max(R_deg_x1[1])
    ax2.plot(R_deg_x1[0], R_deg_x1[1], '.')
    ax2.errorbar(R_deg_x1[0], R_deg_x1[1], yerr = R_deg_x1[2], fmt = 'b.')
    #ax2.set_title(info1['tit2'])
    #ax2.set_ylabel(info1['ylab_1'])
    ax2.set_xlabel(info1['xlab_1']) 
    ax2.set_title('Random con S1 = {} e S2 = {}'.format(S1,S2))
    ax2.grid()
    ax2.set_xlim(-1, S1+1)
    if XM12 < 0.4:
        ax2.set_ylim(-0.1, 0.5)
    else:
        ax2.set_ylim(-0.1, XM12 + 0.1)
    ax2.set_autoscale_on(True)
    
    XM22 = max(R_deg_x2[1])
    ax4.plot(R_deg_x2[0], R_deg_x2[1], '.')
    ax4.errorbar(R_deg_x2[0], R_deg_x2[1], yerr = R_deg_x2[2], fmt = 'b.')
    #ax4.set_ylabel(info1['ylab_2'])
    ax4.set_xlabel(info1['xlab_2']) 
    ax4.grid() 
    ax4.set_xlim(-1, S2+1)
    if XM22 < 0.4:
        ax4.set_ylim(-0.1, 0.5)
    else:
        ax4.set_ylim(-0.1, XM22 + 0.1)
    ax4.set_autoscale_on(True)
    
    import os
    path = "C:/Users/Utente/Anaconda3/Cooperazione//"+dir_name
    os.chdir(path)
    fig.savefig('deg_x_'+name+'.png')
    plt.close()
    
def guess(N1, S1, p, eps, dir_name):
    from ensure_dir import ensure_dir
    file_path = 'C:/Users/Utente/Anaconda3/Cooperazione//'+dir_name+'//guess.txt'
    ensure_dir(file_path)
    V1 = round(1/(S1*p),4)
    Ptot = round(1+ eps*S1*p , 2)
    T_su_P = round(1 - 1/Ptot,2)
    with open(file_path, 'a') as f:
        if f.seek(0,2) == 0:
            print('#N1:   S1:   eps:   p:   V1:  P_tot:   T/P:', file = f)
        print(N1, S1, eps, p, V1, Ptot, T_su_P, sep =  '    ', file=f)
        #if T_su_P == 0:
        #    print('Regime competitivo. \n')
        #if T_su_P < 0.1 and T_su_P > 0:
        #    print('Regime perturbativo. \n')
        #elif T_su_P > 0.1 and T_su_P < 0.5 :
        #    print('Regime misto. \n')
        #else:
        #    print('Regime cooperativo. \n')
        perc = round(T_su_P*100,2)
        print('Regime cooperativo al {} %. \n'.format(perc))
        
def plot_hist2(name, dir_name, rip, N1, N2, info):
    from data_analysis import asymptotic_n
    import matplotlib.pyplot as plt
    import numpy as np
    import statistics as st
    data1 = []
    data2 = []
    b1 = int(N1/5)
    b2 = int(N2/5)
    c_rip_1 = [ [] for x in range(b1)]
    c_rip_2 = [ [] for x in range(b2)]
    for i in range(1,rip+1):
        name1 = 'n1_'+name+'-'+repr(i)
        name2 = 'n2_'+name+'-'+repr(i)
        n1 = asymptotic_n(name1, dir_name)
        n2 = asymptotic_n(name2, dir_name)
        data1 = data1 + n1[:]
        data2 = data2 + n2[:]
        c1, d1, p1 = plt.hist(n1, bins = b1, range = (1,N1), density = True, cumulative = -1)
        plt.close()
        for j in range(len(c1)):
            c_rip_1[j].append(c1[j])
        c2, d2, p2 = plt.hist(n2, bins = b2, range = (1,N2), density = True, cumulative = -1)
        plt.close()
        for j in range(len(c2)):
            c_rip_2[j].append(c2[j])
            
    #print('len(data1) = ', len(data1))
    #print('len(data2) = ', len(data1), '\n')
    
    fig, [ax1, ax2] = plt.subplots(1,2, figsize = (9,5))
    
    counts1, bins1, patches1 = ax1.hist(data1, bins = b1, range = (1,N1), color = 'b',
                                        density = True, cumulative = -1)
    # histtype='step'
    counts2, bins2, patches2 = ax2.hist(data2, bins = b2, range = (1,N2), color = 'b',
                                        density = True,  cumulative = -1)
    
    #print('counts1 = ', counts1)
    #print('counts2 = ', counts2)
    x1 = np.linspace(1, N1, b1)
    x2 = np.linspace(1, N2, b2)
    s1 = []
    s2 = []
    for i in range(len(c_rip_1)):
        s1.append(st.stdev(c_rip_1[i]))
    for i in range(len(c_rip_2)):
        s2.append(st.stdev(c_rip_2[i]))
    ax1.errorbar(x1, counts1, yerr = s1, fmt = 'r.')
    ax1.set_xlabel(info['xlab'])
    ax1.set_ylabel(info['ylab_1'])
    ax1.set_title(info['tit1'])
    ax1.grid()
    ax1.set_autoscale_on(True)
    ax1.set_xlim(1)
    
    ax2.errorbar(x2, counts2, yerr = s2, fmt = 'r.')
    ax2.set_xlabel(info['xlab'])
    ax2.set_ylabel(info['ylab_2'])
    ax2.set_title(info['tit2'])
    ax2.grid()
    ax2.set_autoscale_on(True)
    ax2.set_xlim(1)
    
    import os
    path = "C:/Users/Utente/Anaconda3/Cooperazione//"+dir_name
    os.chdir(path)
    fig.savefig('new_'+name+"_hist.png")
    plt.close()
    
    
    
    
    
    
    
    
def mono_plot(n, name, dir_name, info):
    import matplotlib.pyplot as plt
    
    tau = [x for x in range(len(n))]
    
    #n1 = []
    #n2 = []
    #for i in range(len(n)):
    #    n1.append(n[i][0])
    #    n2.append(n[i][1])
    
    
    plt.plot(tau, n)
    plt.xlabel('Tempo tau [step/N]')
    plt.ylabel('Numero individui')
    plt.title('Voter Model mean field con due specie' )
    plt.xlim(left = 0)
    plt.ylim(bottom = 0)
    plt.grid()
    #plt.set_autoscale_on(True)
    

    import os
    path = "C:/Users/Utente/Anaconda3/Cooperazione//"+dir_name
    os.chdir(path)
    plt.savefig(name+'_plots.png')
    plt.close()
    
    
    
    
    
    
    