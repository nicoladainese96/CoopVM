# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:26:40 2018
Code to test and execute the analyser. There isn't a user interface.
@author: nicola.dainese96@gmail.com
"""

import analyser as an
#at the moment this directory has to be written manually
input_path = 'C:/Users/Utente/Anaconda3/Cooperazione'
x = [0,1,2,3,4,5] #change this list for execute multiple analysis commands
for i in x:
    if i == 0:
        an.e_analyser(input_path)
    if i == 1:
        an.p_analyser(input_path)
    if i == 2:
        an.multiple_p_analyser(input_path)
    if i == 3:
        an.NODF_analyser(input_path)
    if i == 4:
        an.precision_analyser(input_path)
    if i == 5:
        an.S_mean_precision(input_path+'/precision')
print('Test analyser effettuato con successo.')



#just some memo
#import matplotlib as mpl
#mpl.style.available
#plt.style.use('seaborn')
#U+03B5
#u"\u03B5"