# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
def average_above_zero(tab):
    """
    brief : computes the average of the positive values in an array
    Args : 
       tab :  a list of numeric value, expect at list one positive value
    return:
       the computed average as a float value
    raise :
        ValueError if no positive value is found
        ValueError if input tab is not a list
    """
    if not(isinstance(tab, list)):
        raise ValueError('Expected a list as input')
    
    average = -99
    
    valSum = 0.0
    nPositiveValues =0
    NMAX = len(tab) # get the tab length
    # val = each value of the list
    for val in tab:
        if val>0:
            valSum = valSum +float(val)
            nPositiveValues=nPositiveValues+1
    
    if nPositiveValues <=0:
        raise ValueError('No positive value')
    average = valSum/nPositiveValues
    
    return average
    
# Test script
test_tab=[1,2,3,-5]#↨ create a fak tab
moy=average_above_zero(test_tab)
#print('Posivive values average =')
#print(moy)
print('Posivive values average ='+str(moy))
print('Posivive values average ={val}'.format(val=moy))