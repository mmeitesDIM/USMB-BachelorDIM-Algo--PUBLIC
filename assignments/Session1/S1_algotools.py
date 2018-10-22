# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

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

"""
Exercice 2 
"""
"""
 brief : search the maximal value in an array
 Args :  # @tab : the list of values to process
    # @return the max value of the list and his index
 raise :
        ValueError if input tab is empty
"""
def max_value(tab):
    #test if tab is not empty
    if len(tab)==0 :
         raise ValueError('Expected values in tab')

    #initialisation 
    indexValue = 0
    maxValue = tab[0]

    # search max value and his index in array
    for index in range (len(tab)):
        if tab[index]>maxValue :
            maxValue = tab[index]
            indexValue = index 
              

    return float(maxValue),indexValue
        
# Test script
test_tab=[1,2,3,-5]#↨ create a fake tab
maxV, indexV =max_value(test_tab)

#indexV = resultTurple[1]
print('Max value in the imput list =')
print(maxV)
print('index in tab =')
print(indexV)


#message='The max value and his index of  samples of {mylist} is {maxValue),(indexValue)'.format(mylist =test_tab , maxValue =maxV ,indexValue=indexV)
#print(message)
# Test script
test_tab2=[]
maxV, indexV =max_value(test_tab2)

"""
Exercice 3 
"""
from math import *
"""
 brief : reverse order of values in an array
 Args :
    # @tab : the list of values to reverse
    # @return the tab
 raise :
        ValueError if input tab is empty
"""
def reverse_table(tab):
    #test if tab is not empty
    if len(tab)==0 :
         raise ValueError('Expected values in tab')
        
    # initialisation
    max_tab =(len(tab)-1)/2
    nb_turn = int(ceil(max_tab))
    len_tab = len(tab)
               
    for index in range (nb_turn):
        temp_value = tab[index]
        tab[index] = tab[len_tab-1-index]
        tab[len_tab-1-index] = temp_value

    return tab

# Test script
test_tab=[1,2,3,-5]#↨ create a fake tab
tab_result = reverse_table(test_tab)

message='Values of test_tab are {mylist}'.format(mylist =tab_result)
print(message)

# Test script 2
test_tab2=[]
tab_result2 = reverse_table(test_tab2)

"""
Created on Mon Oct 22 11:20:29 2018

@author: meitesm
"""

"""
Bounding box
"""

def roi_bbox(inputMat):
    """TODO : add commentss (what, iputs, outputs) """
    roi = None
    
    # basic input data type to check
    # check if it's a matrice
    if not(isinstance(inputMat, np.ndarray)):
        raise ValueError('Expected a numpy array as input')
    # check if values type is boolean
    if not(inputMat.dtype== np.bool):
        raise ValueError('Expected input of type numpy.binary as input')
        
    """task : find out : cmin, cmax, lmin, lmax
    """
    lmin=inputMat.shape[0]
    lmax=0
    cmin=inputMat.shape[1]
    cmax=0
    
    for l in range(inputMat.shape[0]):
    #.shape = donne la taille de la matrice
    # tuple, on a la  list de la taille de ttes ses dim
        for c in range(inputMat.shape[1]):
            
            if inputMat[l,c]==True:
                if l<lmin:
                    lmin=l
                if l>lmax:
                    lmax=l
                if c<cmin:
                    cmin=c
                if c>cmax:
                    cmax=c
    
    roi=[[lmin, cmin],
         [lmin, cmax],
         [lmax, cmin],
         [lmax, cmax]]              
                    
    return np.array(roi)    # np.array transforme une liste de point en matrice
    
import numpy as np
# creatio d'une matrice de binaire 5 lignes et 5 colonnes de type bool
inputMat = np.zeros((5,6), dtype =np.bool)

#fill some points within it
inputMat[2,3]=True
inputMat[2,4]=True
inputMat[3,3]=True
inputMat[3,4]=True

print('inputMat='+str(inputMat))
roi=roi_bbox(inputMat)
print('roi ='+str(roi))


"""
Exercice de tri Bubble
"""

"""
 brief : sort bubble
  compares 2 values and swap their postion
  if the second is superior to the first one.
 Args :
    # @input_tab : tab of values to sort
    # @return a sorted tab
 raise :
     ValueError if input tab is empty
"""
def sort_bubble( input_tab):
    #test if list is not empty
    if len(input_tab)==0 :
        raise ValueError('Expected values in tab')
 

    #initialisation 
    array_sorted = False
    len_tab = len(input_tab)
    index=0

    while(array_sorted == False):
        array_sorted = True
        for index in range (len_tab-1):
            if input_tab[index] > input_tab[index+1]:
                tmp_value = input_tab[index]
                input_tab[index] = input_tab[index+1]
                input_tab[index+1] = tmp_value
                array_sorted = False
                          
        len_tab -=1
    
        
    return input_tab

# Test script
test_tab = [10,15,7,1,3,3,9]#↨ create a vector sample
print('Values of test_tab are : {}'.format(test_tab))
result_tab = sort_bubble(test_tab)
message='After bubble sort : {}'.format(result_tab)
print(message)

#test 2
test_tab2 = []
result_tab = sort_bubble(test_tab2)

