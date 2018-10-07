# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 08:30:32 2018

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
        