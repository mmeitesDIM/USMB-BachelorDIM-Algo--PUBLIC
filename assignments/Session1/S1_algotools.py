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
        
    for index in range (len(tab)):
        if (isinstance(tab[index],str)):
             raise ValueError('String not allowed as Input')  
    
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
            
    for index in range (len(tab)):
        if (isinstance(tab[index],str)):
             raise ValueError('String not allowed as Input') 

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
import numpy as np
"""
 brief : reverse order of values in an array
 Args :
    # @tab : the list of values to reverse
    # @return the tab
 raise :
        ValueError if input tab is empty
"""
def reverse_table(tab):
 #basic input data type check
    if not (isinstance(tab, list)):
        raise ValueError('Expected a list as Input')
    
    for index in range (len(tab)):
        if (isinstance(tab[index],str)):
             raise ValueError('String not allowed as Input') 
                
    #test if tab is not empty
    if len(tab)==0 :
         raise ValueError('Expected values in tab')
        
    # initialisation
    max_tab = len(tab)
    nb_turn = int(np.floor(max_tab/2))
    len_tab = -1
               
    for index in range (nb_turn):
        temp_value = tab[len_tab-index]
        tab[len_tab-index] = tab[index]
        tab[index] = temp_value

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
    """
    brief : find coordonnates (top left, top right, bottom left, bottom right) of an image
    Args :
        @inputMat : 2D matrix with binary values
        @return :  the bounding box coordinates of the object. 
    raise :
        ValueError if input data type is not binary
        ValueError if input data type is not a numpy array
    """
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
# creatio d'une matrice de binaire 5 lignes et 6 colonnes de type bool
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
Exercice 6
"""
"""
 brief : remove whitespace caracter in a string
 Args :
    # @input_string : the string to remove whitespace
    # @return the string without whitespace
 raise :
"""

def remove_whitespace(input_string):
    if len(input_string)==0:
        print('aucune chaîne de caractère en entrée')

    tmp_char =""
    list_index = []
    #list_index[0] = 0
    result_string=""
    tmpElt = 0
    
    # search whitespace caracter index in input_string
    for index in range (len(input_string)):
        tmp_char = input_string[index]

        if tmp_char ==" " :
            list_index.append(index);
            
    # delete  whitespace caracter        
    for index in range (len(input_string)):            
        for elt in list_index:
            if index == elt:
            
                if result_string=="":
                    result_string = input_string[:elt]
                else:
                    result_string += input_string[tmpElt:elt]
            tmpElt = elt+1
  
    result_string += input_string[tmpElt:]
    return result_string         
            
# Test script
test_string = 'il en faut peu pour etre heureux'#↨ create a fake tab
result_string = remove_whitespace(test_string)
print(result_string)



"""
Exercice de tri sélectif
"""
"""
 brief : selective sort
  compares 2 values and swap their postion
  if the second is inferior to the first one.
 Args :
    # @input_tab : tab of values to sort
    # @return a sorted tab
 raise :
     ValueError if input tab is empty
"""
def sort_selective( input_tab):
    
    if len(input_tab)==0 :
        raise ValueError('Expected values in tab')
 
    # initialisation
    len_tab = len(input_tab)
    min_position = 0
    
    for index_i in range (len_tab):
        min_position = index_i
        
        for index_j in range(index_i+1 ,(len_tab)):
            # search the smallest value 
            if input_tab[index_j]<input_tab[min_position]:
                 min_position = index_j
                 
        # swap
        tmp_value = input_tab[min_position]
        input_tab[min_position] = input_tab[index_i]
        input_tab[index_i] = tmp_value

    return input_tab
    
# Test script
test_tab = [10,15,7,1,3,3,9]#↨ create a vector sample
print('Values of test_tab are : {}'.format(test_tab))
result_tab = selective_sort(test_tab)
print('result_tab = {}'.format(result_tab))

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

