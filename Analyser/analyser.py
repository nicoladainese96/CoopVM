# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:00:29 2018

@author: Utente
"""
def NODF_analyser(input_path):
    import my_input as I
    #import my_output as O
    pstrings = I.csv_string_reader ('info_NODF', input_path)
    for i in range(len(pstrings)):
        print('Analisi riga {} NODF - string.'.format(i+1))
        NODF2_analyser(pstrings[i])
        #O.p_hist(pstrings[i])
        
def NODF2_analyser(data):
    #import my_input as I
    import my_output as O
    import math
    NODF_len = (len(data) - 6)
    NODFs = []
    
    parent_dir = data[0]
    N =  int(data[1])
    S1 = int(math.sqrt(N))
    S2 = int(math.sqrt(N))
    rip = data[2]
    for j in range(NODF_len):
        y = float(data[3+j])
        NODFs.append(y)  
    eps = data[-3]
    C = data[-2]
    #tau = data[-1]
    (S1_m_l, S1_d_l) = NODF_S_analysis('S1_', parent_dir, eps, C, NODFs)
    (S2_m_l, S2_d_l) = NODF_S_analysis('S2_', parent_dir, eps, C, NODFs)
    O.NODF_print(S1_m_l, S1_d_l, S2_m_l, S2_d_l, eps, C, NODFs, S1, S2, rip, parent_dir)
    

def p_analyser(input_path):
    import my_input as I
    import my_output as O
    pstrings = I.csv_string_reader ('info_p', input_path)
    for i in range(len(pstrings)):
        print('Analisi riga {} pstring.'.format(i+1))
        p2_analyser(pstrings[i])
        #O.p_hist(pstrings[i])
        
def p2_analyser(data):
    #import my_input as I
    import my_output as O
    import math
    ps_len = (len(data) - 5)
    ps = []
    
    parent_dir = data[0]
    N =  int(data[1])
    S1 = int(math.sqrt(N))
    S2 = int(math.sqrt(N))
    #rip = data[2]
    eps =  data[3]
    for j in range(ps_len):
        y = float(data[4+j])
        ps.append(y)  
    #tau = data[-1]
    #attenzione: da cambiare S_analysis, vd e2_analyser
    #Prova:
    #ps = ps = [0.0, 0.033, 0.066, 0.1, 0.2, 0.35, 0.5]
    (N_S1_m_l, N_S1_d_l) = p_S_analysis('N_S1_', parent_dir, eps, ps)
    (N_S2_m_l, N_S2_d_l) = p_S_analysis('N_S2_', parent_dir, eps, ps)
    (R_S1_m_l, R_S1_d_l) = p_S_analysis('R_S1_', parent_dir, eps, ps)
    (R_S2_m_l, R_S2_d_l) = p_S_analysis('R_S2_', parent_dir, eps, ps)
    #print('len(N_S1_m_list) = ', len(N_S1_m_l))
    #print('len(N_S1_d_list) = ', len(N_S1_d_l), '\n')
    O.C_print(ps, N_S1_m_l, N_S1_d_l, N_S2_m_l, N_S2_d_l, 
              R_S1_m_l, R_S1_d_l, R_S2_m_l, R_S2_d_l, 
              eps, parent_dir, S1, S2, eps)
    



def e_analyser(input_path):
    #una riga è sufficiente ad una analisi!!
    import my_input as I
    import my_output as O
    estrings = I.csv_string_reader ('info_e', input_path)
    print(estrings)
    print(estrings[0])
    for i in range(len(estrings)):
        print('Analisi riga {} estring.'.format(i+1))
        e2_analyser(estrings[i])
        #O.e_hist(estrings[i])
     

def e2_analyser(data):
    #import my_input as I
    import my_output as O
    import math
    
    eps_len = (len(data) - 5)
    epsilons = []
    
    parent_dir = data[0]
    N =  int(data[1])
    S1 = int(math.sqrt(N))
    S2 = int(math.sqrt(N))
    #rip = data[2]
    for j in range(eps_len):
        y = float(data[3+j])
        epsilons.append(y)
    
    p = data[-2]
    #tau = data[-1]
        
    (N_S1_m_l, N_S1_d_l) = e_S_analysis('N_S1_', parent_dir, epsilons, p)
    (N_S2_m_l, N_S2_d_l) = e_S_analysis('N_S2_', parent_dir, epsilons, p)
    (R_S1_m_l, R_S1_d_l) = e_S_analysis('R_S1_', parent_dir, epsilons, p)
    (R_S2_m_l, R_S2_d_l) = e_S_analysis('R_S2_', parent_dir, epsilons, p)
    
    O.eps_print(epsilons, N_S1_m_l, N_S1_d_l, N_S2_m_l, N_S2_d_l, 
              R_S1_m_l, R_S1_d_l, R_S2_m_l, R_S2_d_l, 
              p, parent_dir, S1, S2, p)
    
    
def e_S_analysis(name, parent_dir, epsilons, p):
    import my_input as I
    print('name = ', name)
    print('parent_dir = ', parent_dir)
    Istring = I.csv_string_reader (name+'files', parent_dir)
    S_means = []
    S_devs = []
    
    if len(epsilons) != len(Istring):
        print('Attenzione len(epsilons) != len(Istring): ')
        print('len(epsilons) = ', len(epsilons))
        print('len(Istring) = ', len(Istring), '\n')
        #print('Istring = ', Istring)
    for i in range(len(epsilons)):
        eps = epsilons[i]
        print('Istring[{}] = '.format(i), Istring[i], '\n')
        (S_mean, S_dev) = S_mean_asymptotic(name, Istring[i], eps, p)
        S_means.append(S_mean)
        S_devs.append(S_dev)
        
    return (S_means, S_devs)

def p_S_analysis(name, parent_dir, eps, ps):
    import my_input as I
    
    Istring = I.csv_string_reader (name+'files', parent_dir)
    S_means = []
    S_devs = []
    if len(ps) != len(Istring):
        print('Attenzione len(ps) != len(Istring): ')
        print('len(ps) = ', len(ps))
        print('len(Istring) = ', len(Istring), '\n')
    for i in range(len(ps)):
        p = ps[i]
        (S_mean, S_dev) = S_mean_asymptotic(name, Istring[i], eps, p)
        S_means.append(S_mean)
        S_devs.append(S_dev)
        
    return (S_means, S_devs)

def NODF_S_analysis(name, parent_dir, eps, p, NODFs):
    import my_input as I
    Istring = I.csv_string_reader (name+'files', parent_dir)
    S_means = []
    S_devs = []
    #if len(NODFs) != len(Istring):
        #print('Attenzione len(ps) != len(Istring): ')
        #print('len(NODFs) = ', len(NODFs))
        #print('len(Istring) = ', len(Istring), '\n')
    for i in range(len(NODFs)):
        NODF = NODFs[i]
        (S_mean, S_dev) = S_mean_asymptotic2(name, Istring[i], eps, p, NODF)
        S_means.append(S_mean)
        S_devs.append(S_dev)
        
    return (S_means, S_devs)

def S_mean_asymptotic(name, data_string, eps, p):
    import statistics as stat
    import math
    S_m = []
    rip = len(data_string) - 1
    filenames = data_string[1:]
    #print('filenames = ', filenames)
    #print('rip = ', rip)
    for i in range(rip):
        x = asymptotic_S(name, filenames[i], data_string[0], i, float(eps) , float(p))
        S_m.append(x)
    N = len(S_m)
    S_mean = round(stat.mean(S_m),2)
    S_dev = round(stat.stdev(S_m)/math.sqrt(N),2)
    
    return (S_mean, S_dev)


def S_mean_precision( work_dir):
    #name = 'S1_' o 'S2_'
    #work_dir = /precision
    #Sia per S1 che per S2 devo avere la stima media dei valori asintotici
    #per la simulaizone nuova e per quella vecchia
    import my_input as I
    import math
    import matplotlib.pyplot as plt
    refN_1 = I.csv_string_reader('S1_files', work_dir)[0]
    refV_1 = I.csv_string_reader('S1_files', work_dir)[1] 
    refN_2 = I.csv_string_reader('S2_files', work_dir)[0]
    refV_2 = I.csv_string_reader('S2_files', work_dir)[1]
    (S1_N, d1_N) = S_ref(refN_1)
    print('S1_N = ', round(S1_N,3))
    print('d1_N = ', round(d1_N,3))
    (S1_V, d1_V) = S_ref(refV_1)
    print('S1_V = ', round(S1_V,3))
    print('d1_V = ', round(d1_V,3))
    (S2_N, d2_N) = S_ref(refN_2)
    print('S2_N = ', round(S2_N,3))
    print('d2_N = ', round(d2_N,3))
    (S2_V, d2_V) = S_ref(refV_2)
    print('S2_V = ', round(S2_V,3))
    print('d2_V = ', round(d2_V,3))
    S_N = S1_N + S2_N
    print('S_N = ', round(S_N,3))
    S_V = S1_V + S2_V
    print('S_V = ', round(S_V,3))
    d_N = math.sqrt( (pow(d1_N,2)+ pow(d2_N,2) ))
    print('d_N = ', round(d_N,3))
    d_V = math.sqrt( (pow(d1_V,2)+ pow(d2_V,2) ))
    print('d_V = ', round(d_V,3))
    l = abs(S_N - S_V)/ math.sqrt( (pow(d_V,2)+ pow(d_N,2) ))
    print('deltaS = ', round(abs(S_N - S_V),3))
    print('deltaS/S = ', round(abs(S_N - S_V)/20,3))
    print('sigma deltaS = ',  round(math.sqrt( (pow(d_V,2)+ pow(d_N,2) )),3))
    print('sigma deltaS/S = ',  round(math.sqrt( (pow(d_V,2)+ pow(d_N,2) ))/20,3))
    print('lambda = ', round(l,3))
    
    
def S_ref (ref):
    import statistics as stat
    import math
    dir_name = ref[0]
    filenames = ref[1:]
    S_m1 = []
    for i in range(len(filenames)):
        x = asymptotic_S1(filenames[i], dir_name, i)
        S_m1.append(x)
    N = len(S_m1)
    #print('N = ', N, '\n')
    S_mean = round(stat.mean(S_m1),2)
    S_dev = round(stat.stdev(S_m1)/math.sqrt(N),2)
    
    return (S_mean, S_dev)
    
def S_mean_asymptotic2(name, data_string, eps, p, NODF):
    import statistics as stat
    import math
    S_m = []
    rip = len(data_string) - 1
    filenames = data_string[1:]
    print('filenames = ', filenames)
    print('rip = ', rip)
    for i in range(rip):
        x = asymptotic_S2(name, filenames[i], data_string[0], i, float(eps) , float(p), float(NODF))
        S_m.append(x)
    N = len(S_m)
    print('N = ', N, '\n')
    S_mean = round(stat.mean(S_m),2)
    S_dev = round(stat.stdev(S_m)/math.sqrt(N),2)
    
    return (S_mean, S_dev)
    
def asymptotic_S(name, filename, dir_name, re, eps, p):
    import my_input as I
    import my_output as O
    import statistics
    v = I.csv_reader2(filename, dir_name)
    tau_tot = len(v)
    tau_start = int(tau_tot*9/10)
    S_as = []
    for i in range(tau_start,tau_tot):
        S_as.append(v[i][0])
    if re == 0:
        S = []
        for i in range(0,tau_tot):
            S.append(v[i][0])
        O.S_plot(S, eps, p, name, dir_name)
    
    S_mean = statistics.mean(S_as)
    return S_mean

def asymptotic_S1(filename, dir_name, re):
    import my_input as I
    import statistics
    v = I.csv_reader2(filename, dir_name)
    tau_tot = len(v)
    tau_start = int(tau_tot*9/10)
    S_as = []
    for i in range(tau_start,tau_tot):
        S_as.append(v[i][0])
    S_mean = statistics.mean(S_as)
    return S_mean

def asymptotic_S2(name, filename, dir_name, re, eps, p, NODF):
    import my_input as I
    import my_output as O
    import statistics
    v = I.csv_reader2(filename, dir_name)
    tau_tot = len(v)
    tau_start = int(tau_tot*9/10)
    S_as = []
    for i in range(tau_start,tau_tot):
        S_as.append(v[i][0])
    if re == 0:
        S = []
        for i in range(0,tau_tot):
            S.append(v[i][0])
        O.S_plot2(S, eps, p, NODF, name, dir_name)
    
    S_mean = statistics.mean(S_as)
    return S_mean

def n_analysis2 (name, parent_dir):
    #se restituisco solo medie di medie non posso fare l'istogramma delle frequenze!
    import my_input as I
    Istring = I.csv_string_reader (name+'files', parent_dir)
    #print('Istring = ', Istring, '\n')
    v_n_rips = []
    for i in range(len(Istring)):
        v_n_rip = ns_mean_asymptotic(Istring[i])
        v_n_rips.append(v_n_rip)
        
    return v_n_rips

def ns_mean_asymptotic(data_string):
    v_n_rip = []
    rip = len(data_string) - 1
    filenames = data_string[1:]
    #print('filenames = ', filenames, '\n')
    for i in range(rip):
        x = asymptotic_n(filenames[i], data_string[0])
        v_n_rip.append(x)    
    return (v_n_rip)

def asymptotic_n (name, dir_name):
    #analisi per una singola realizzazione
    #print('name = ', name, '\n')
    #print('dir_name = ', dir_name, '\n')
    
    #import my_print as my
    import my_input as I
    import statistics as st
    #n = my.tab_reader2(name, dir_name)  
    n = I.csv_reader2(name, dir_name)
    m = [ [] for x in range( len(n[0]) )]
    for i in range(int(len(n)/2), len(n) ):
        for j in range(len(n[0]) ):
            m[j].append(n[i][j] )
    x = []
    for i in range(len(m)):
        x.append(st.mean(m[i]) )
        
    return x
    