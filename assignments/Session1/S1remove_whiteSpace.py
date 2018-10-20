# -*- coding: utf-8 -*-

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
