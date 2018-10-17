# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 11:13:36 2018
t_conv is a function that given a certain N (total number of individuals in a VM)
returns a proper time of simulation (number of steps) t_conv so that, if both cooperation
and speciation are null, in that time the VM converges to mono-dominance in most cases.
What "most cases" means depends on the formula chosen to compute t_conv from 5 
test simulations with both nu and epsilon null. 
@author: nicola.dainese96@gmail.com
"""

def t_conv(N, m = 1, s = 5):
    #t_conv = m*t_mean + s*stdev(t)
    from init_simulation import init_simulation
    import statistics as stat
    t = []
    for i in range(5):
        #this init_simulation has to be changed to the one below
        t_i = init_simulation(N)
        t.append(t_i)
    t_mean = stat.mean(t)
    t_dev = stat.stdev(t)
    print('t_mean = ', round(t_mean,1))
    print('t_dev = ', round(t_dev,1))
    t_conv = int(round(m*t_mean + s*t_dev, 0))
    print('t_conv = {}*t_mean + {}*t_dev = '.format(m,s), t_conv, '\n')
    
    return t_conv

def init_simulation_2(N):
    #this has to be implemented in numpy
    import math
    from random import randint
    from copy import deepcopy
    S = int(math.sqrt(N))
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