def init_simulation(N):
    import math
    from random import randint
    from copy import deepcopy
    S = int(math.sqrt(N))
    #print("S = {}".format(S))
    nu = 0
    v = [ randint(0, S-1) for x in range (0,N)]
    n = []
    Smax = max(v)
    for i in range (0,Smax+1):
        c = v.count(i)
        n.append(c)

    from one_step_bi import one_step_mono
    t_conv = 0
    i = 0
    while t_conv == 0:
        i = i + 1
        (v,n) = one_step_mono(N, nu, v, n, i)
        n1 = deepcopy(n)
        S = len(n1) - n1.count(0)
        if S == 1:
            print("Convergenza raggiunta allo step {}.".format(i))
            t_conv = i

    return t_conv

def init_simulation2(N, S, dir_name, name):
    #import math
    import numpy as np
    from random import randint
    from copy import deepcopy
    import my_print as my
    #S = int(math.sqrt(N))
    #print("S = {}".format(S))
    nu = 0
    v = [ randint(0, S-1) for x in range (0,N)]
    n = []
    Smax = max(v)
    for i in range (0,Smax+1):
        c = v.count(i)
        n.append(c)
    #@@@@@@@@@@@
    v = np.random.randint(0,S,N)
    n = np.zeros(S,dtype=int)
    index, counts = np.unique(v, return_counts=True)
    for i in range(len(index)):
        n[index[i]] = counts[i]
    #@@@@@@@@@@@
    from one_step_bi import one_step_mono
    t_conv = 0
    i = 0
    while t_conv == 0:
        i = i + 1
        for j in range(N):
            (v,n) = one_step_mono(N, nu, v, n, i)
        
        n1 = deepcopy(n)
        my.print_tuple(n, 'n_'+name, dir_name, d = len(n))
        S = len(n1) - n1.count(0)
        if S == 1:
            print("Convergenza raggiunta a tau {}.".format(i))
            t_conv = i

    v_n = my.tab_reader2('n_'+name, dir_name)
    info = {}
    my.mono_plot(v_n, name, dir_name, info)