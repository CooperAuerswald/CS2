'''
Author: Cooper Auerswald
Date: 9/30/2025
Description: Practicing functions for CS2 Class
Bugs: returns first name as doctor - middle name and last name dont work if mulitple middle names - 
Challenges: sorted array of characters, menu, title boolean,  
Sources: Mr. Cambell
Log: 1.0 Initial Release
'''

import random

def reverse(name):
    '''
    Description: takes the name, and reverses it

    Args:
        name(str): the original name input
    Returns:
        reversed_name (str) the name, but in reverse.'''
    reversed_name = name[::-1]
    return reversed_name

def count_vowels(name):
    '''
    Description: counts the total number of vowels

    Args:
        name(str): the original name input
    Returns:
        vowels: counter of the number of vowels.
        '''
    
    vowels = 0          

    for c in name:                                      
        if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E','I','O','U']:                                     
            vowels += 1                                     
    return vowels

def count_consonants(name):
    '''
    Description: counts the total number of consonants

    Args:
        name(str): the original name input
    Returns:
        consonants: counter of the number of consonants.
        '''
    consonants = 0

    for c in name:                                      
        if c not in ['a', 'e', 'i', 'o', 'u', 'A', 'E','I','O','U']:                                     
            consonants += 1                                     
    return consonants
    
def first_name(name): #run title function, if true, make first name index 1 instead of 0, if false, name index 0
    '''
    Descripiton: separates out the first name

    Args:
        name(str): the original name input
    Returns:
        names[0]: the first in the list of names
        '''
    names=name.split(" ")
    return(names[0])

def last_name(name):
    '''
    Description: separates out the last name

    Args:
        name(str): the original name input
    Returns:
        names[2]: the last in the list of names
        '''
    names=name.split(" ")
    return(names[2])

def middle_name(name):
    '''
    Description: separates out the middle name

    Args:
        name(str): the original name input
    Returns:
        names[1]: the second in the list of names
        '''
    names=name.split(" ")
    return(names[1])

def hyphenated (name):
    '''
    Description: returns a boolean if there is a hyphen in the name

    Args:
        name(str): the original name input
    Returns:
        status1: whether or not the name has a hyphen
        '''
    hyphen ="-"
    if hyphen in name:
        status1=("True")
    else:
        status1=("False")
    return (status1)

def lowercase(name):
    '''
    Description: converts the whole name to lowercase, similar to string.lower

    Args:
        name(str): the original name input
    Returns:
        name_out: name in all lowercase
        '''
    name_out=" "
    for letter in name:
        if ord (letter) >64 and ord(letter) <91:
            num=ord(letter)
            num=num+32
            letter=chr(num)
            name_out=name_out+letter
        else:
           name_out=name_out+letter
    return (name_out)

def uppercase(name):
    '''
    Description: converts the whole name to uppercase, similar to string.upper

    Args:
        name(str): the original name input
    Returns:
        name_out1: output in uppercase
        '''
    name_out1=" "
    for letter1 in name:
        if ord (letter1) >=97 and ord(letter1) <=122:
            num1=ord(letter1)
            num1=num1-32
            letter1=chr(num1)
            name_out1=name_out1+letter1
        else:
           name_out1=name_out1+letter1
    return (name_out1)

def shuffle(name):   
    '''
    Description: scrambles all characters in the name, including spaces.

    Args:
        name(str): the original name input
    Returns:
        shuffled: shuffled name
        '''       
    shuffled=""
    letters=list(name)

    while len(letters) >0:
        letter=random.choice(letters)
        shuffled+=letter
        letters.remove(letter)
    return(shuffled)

def palindrome(name):
    '''
    Description: Returns a boolean if the name is or is not a palindrome

    Args:
        name(str): the original name input
    Returns:
        status: true or false
        '''
    lower_name = lowercase(name)
    reverse_name = reverse(lower_name)
    if reverse_name == lower_name:
        return True
    else:
        return False


def title(name): # finish documentation when done
    '''  
    Description: Returns a boolean if the name has a palindrome

    Args:
        name(str): the original name input
    Returns:
        
    
        '''
    titles=['Dr.', 'Mr.', 'Sir', 'Ms.', 'Mrs.', 'Jr.', 'Sr.','PhD.','MD','III']
    for title in titles:
        if title in name:
            return True
    return False
        
def initials(name):
    '''
    Description: Returns inditials of the name

    Args:
        name(str): the original name input
    Returns:
        Initials: Initials of the name
        '''
    name= name.split(' ')
    initials = ""
    for name in name:
        initials += name [0]
    return initials

def sort(name):
    #turn to list
    '''
    Description: returns a sorted array of characters

    Args:
        name(str): the original name input
    Returns:
        order: the sorted array as a string
        '''
    order = ' '
    real_name = name.replace(' ', '')
    chars = list(real_name)
    sorted_chars=sorted(chars)
    order = order = sorted_chars
    return (order)

def main (): #WHAT WOULD RETURNS BE
    '''
    Description: main menu function

    Args:
        name(str): the original name input
        selection(str): The choice of function to run
    Returns:
        
        '''
    name=input ("What is your full name? ")
    while True:
        selection=input ('''
What would you like to do? (q to quit)
1. Reverse☑️
2. Count Vowels☑️
3. Consonant frequency☑️
4. First Name☑️
5. Last Name☑️
6. Middle Name☑️
7. Hyphen?☑️
8. Convert to Lowercase☑️
9. Convert to Uppercase☑️
10. Scramble☑️
11. Palindrome?☑️
12. Sorted Array☑️
13. Initials☑️
14. Title?
                         ''')
        if selection == ("q"):
            break
        elif selection == ("1"): 
          print(reverse(name))
        elif selection == ("2"):
            print(count_vowels (name))
        elif selection == ("3"):
            print(count_consonants (name))
        elif selection == ("4"):
            print(first_name (name))
        elif selection == ("5"):
            print(last_name (name))
        elif selection == ("6"):
           print(middle_name(name))
        elif selection == ("7"):
            print(hyphenated (name))
        elif selection == ("8"):
            print(lowercase(name))
        elif selection == ("9"):
            print(uppercase(name))
        elif selection == ("10"):
            print(shuffle(name))
        elif selection == ("11"):
            print(palindrome(name))
        elif selection == ("12"):
            print(sort(name))
        elif selection ==("13"):
            print (initials(name))
        elif selection == ("14"):
            print (title(name))
        else:
            print ("Invalid Response")
        

main()
        