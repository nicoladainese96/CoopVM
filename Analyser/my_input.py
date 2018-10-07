# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 08:30:17 2018
Code for reading both csv data and strings.
@author: nicola.dainese96@gmail.com
"""


def csv_reader (filename, dir_path):
    from ensure_dir import ensure_dir
    file_path = dir_path+'//'+ filename + ".csv"
    ensure_dir(file_path)
    with open (file_path, 'r') as f:
        l = []
        l2 = []
        T = 0
        while T == 0:
            s = f.readline().split(',')
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

def csv_reader2 (filename, dir_path):
    from ensure_dir import ensure_dir
    file_path = dir_path+'/data_plot/'+ filename 
    ensure_dir(file_path)
    with open (file_path, 'r') as f:
        l = []
        l2 = []
        T = 0
        while T == 0:
            s = f.readline().split(',')
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

def csv_string_reader (filename, dir_path):
    from ensure_dir import ensure_dir
    file_path = dir_path+'//'+ filename + ".csv"
    ensure_dir(file_path)
    with open (file_path, 'r') as f:
        l = []
        l2 = []
        T = 0
        while T == 0:
            s = f.readline().split(',')
            if s[0] != '':
                d = len(s)
                l2 = []
                for i in range(0,d-1):
                    l2.append(s[i])
                z = s[d-1].split('\n')
                l2.append(z[0])
                l.append(l2)
            else:
                T = 1
                break
    return l

