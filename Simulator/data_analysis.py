"""
Just needed because of my_print. 
"""

def asymptotic_S_1(t_S, nu, N, flag = False, t_start = 1):
    """ """
    import statistics
    import math
    t = t_S[-1][0]
    if flag == False:
        c = math.exp(-nu*N/10)
        t_start = int(0.6*c*t)

    S = []
    for i in range(t_start,t):
        S.append(t_S[i][1][0])
    S_mean = statistics.mean(S)
    return S_mean

def asymptotic_deg_n (N, name1, name2, dir_name, tau_start):
    import my_print as my
    import statistics as st
    
    S_deg = my.tab_reader2(name2, dir_name)
    
    n = my.tab_reader2(name1, dir_name)  
    m = [ [] for x in range( len(n[0]) )]
    for i in range(tau_start, len(n) ):
        for j in range(len(n[0]) ):
            m[j].append(n[i][j]/N )
    x = []
    for i in range(len(m)):
        x.append(st.mean(m[i]) )
    deg_n = []
    deg = []
    for i in range(len(S_deg)):
        deg.append(S_deg[i][1])
    M = max(deg)
    #print('len(deg) = ', len(deg))
    #print('x = ', x)
    #print('S_deg = ', S_deg)
    #print('deg = ', deg)
    if len(S_deg) != len(x):
        print('Attenzione: len(S_deg) = {} e len(x) = {} '.format(len(S_deg),len(x)))
        print('S_deg = ', S_deg)
        print('x = ', x)
    for j in range(0, M+1):
        #print('j = ', j)
        for i in range(len(S_deg) ):
            if deg[i] == j:
                deg_n.append( (S_deg[i][1], x[i]) )
                
    return deg_n

def asymptotic_n (name, dir_name):
    import my_print as my
    import statistics as st
    n = my.tab_reader2(name, dir_name)  
    m = [ [] for x in range( len(n[0]) )]
    for i in range(int(len(n)/2), len(n) ):
        for j in range(len(n[0]) ):
            m[j].append(n[i][j] )
    x = []
    for i in range(len(m)):
        x.append(st.mean(m[i]) )
        
    return x

def Pn_cumulative (t_S, t_n, nu, N, flag = False, first = 0):
    """ """
    import statistics
    import time
    import math
    
    start = time.time()
    t = t_S[-1][0] 
    if flag == False:
        c = math.exp(-nu*N/10)
        t_start = int(0.6*c*t)
    else:
        t_start = first
    Pn_t = [ [] for x in range(0,N)]
    for i in range(t_start,t):
        S = t_S[i][1][0]
        n = t_n[i][1][:]
        Pm = compute_Pn_t(S, n, N)
        for y in range(0,len(Pm)):
            Pn_t[y].append(Pm[y])
    Pn_mean = []
    for i in range(0, len(Pn_t)):
        m = statistics.mean(Pn_t[i])
        Pn_mean.append(m)

    return Pn_mean
    finish = time.time()
    t_tot = round(finish-start,2)
    print("Tempo analisi per P(n) = {}".format(t_tot))
    
def Pn_cumulative2 (n, N, t_start):
    import statistics as stat
    t_max = len(n)
    S_max = len(n[0])
    fn_t = [ [] for x in range(0,N)]
    Pc_mean = []
    for i in range(t_start,t_max):
        S = S_max - n[i].count(0)
        #fn è una lista lunga N
        fn = compute_fn(S, n[i], N)
        for j in range(N):
            fn_t[j].append(fn[j])
    fn_mean = []
    for i in range(N):
        fn_mean.append(stat.mean(fn_t[i]))
    check = 0
    for i in range(len(fn_mean)):
        check = check + fn_mean[i]
    if round(check,4) != 1:
        print('Attenzione Pn_cumulative2: Ptot = ', round(check,4))
        
    Pc = 1
    Pc_mean.append(Pc)
    for i in range(len(fn_mean)-1):
        
        Pc = Pc - fn_mean[i]
        Pc_mean.append(Pc)
    #bisognerebbe controllare quanto vale fn_mean[0] e a cosa corrisponde!
        
    return Pc_mean

def compute_Pn_t(S, n, N):
    """ """
    n.sort()
    n.reverse()
    m = n[:S]
    m.reverse()
    M = max(m)
    Pm = [1] #P>(n), vale 1 per n=1
    #attenzione agli indici, 0 deve corrispondere a n = 1
    for i in range(1,M):
        Q = m.count(i)
        p = Q/S
        P = Pm[i-1] - p
        Pm.append(P) #elemento i-esimo di Pm (len(Pm)=i)
    for i in range(0, N-M):
        Pm.append(0)   
    return Pm
        
def t_start(t_S, eps, N):
    #import math
    t = t_S[-1][0] 
    #ricalibrare formula
    #c = math.exp(-eps*N/10)
    #t_start = int(0.6*c*t)
    t_start = t/2
    return int(t_start)

def Pn(n, N, t_start):
    import statistics as stat
    t_max = len(n)
    S_max = len(n[0])
    fn_t = [ [] for x in range(0,N)]
    for i in range(t_start,t_max):
        S = S_max - n[i].count(0)
        #fn è una lista lunga N
        fn = compute_fn(S, n[i], N)
        for j in range(N):
            fn_t[j].append(fn[j])
    fn_mean = []
    for i in range(N):
        fn_mean.append(stat.mean(fn_t[i]))
    return fn_mean
    
        

def compute_fn (S, n, N):
    n.sort()
    n.reverse()
    m = n[:S]
    m.reverse()
    M = max(m)
    fn = [] 
    #attenzione agli indici, 0 deve corrispondere a n = 1
    for i in range(1,M+1):
        Q = m.count(i)
        p = Q/S
        fn.append(p) #elemento i-esimo di Pm (len(Pm)=i)
    for i in range(0, N-M):
        fn.append(0)   
    P_tot = 0
    for i in range(len(fn)):
        P_tot = P_tot + fn[i]
    if round(P_tot,4) != 1:
        print('fn tot = ', P_tot)
    return fn
    
        
    






    
