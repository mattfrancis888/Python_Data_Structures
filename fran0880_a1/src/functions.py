'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-01-12"
-------------------------------------------------------
'''
def substitute(string, ciphertext):
    """
    -------------------------------------------------------
    Encipher a string using the letter positions in ciphertext.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = substitute(string, ciphertext):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        ciphertext - ciphertext alphabet (str)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    string = string.upper()
    ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    estring = ''
    for char in string:
        if char in ALPHABET:
            alphabet_index = ALPHABET.find(char)
            estring += ciphertext[alphabet_index]
        else:
            estring+=char
            
    write_file = open('substitute.txt', 'w', encoding = 'utf-8')
    print(estring, file = write_file)
    
    return estring
def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    string = string.upper()
    ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    estring =''
    for char in string:
        if char in ALPHABET:
            char_index = ALPHABET.find(char) + n
            while char_index >= len(ALPHABET):
                char_index = char_index - (len(ALPHABET))
            estring += ALPHABET[char_index]  
        else:
            estring += char  
    
    write_file = open('shift.txt', 'w', encoding = 'utf-8')
    print(estring, file = write_file)
    
    return estring

def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """

    palindrome = False
    index=0
    reversed_index = -1
    #convert to lower to ignore case
    s = s.lower()
    s = s.replace(' ','')
    PUNCTUATIONS = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    new_s = ''
    #get rid of punc
    for char in s:
        if char not in PUNCTUATIONS:
            new_s += char

    
    while index < (len(new_s) // 2) and new_s[index] == new_s[reversed_index]:
        index+=1
        reversed_index -= 1

    if index == (len(new_s) // 2):
        palindrome = True
    return palindrome
        
    
def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
        else:
            leap_year = True
    return leap_year
def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a (int)
    -------------------------------------------------------
    """
    md = 0
    for i in range(1, len(a)):
        diff =  abs(a[i] - a[i-1])
        if diff > md:
            md = diff
    return md
def transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b=[]
    
    for i in range(len(a[0])):
        temp = []
        for x in a:
            temp.append(x[i])
        b.append(temp)
    
    return b
    
def rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    Use: ra = rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of float)
    Returns:
        ra - the rotated 2D list of values (2D list of float)
    -------------------------------------------------------
    """
    ra=[]
    for i in range(len(a[0])):
        temp = []
        for x in reversed(a):
            temp.append(x[i])
        ra.append(temp)
    
    return ra    
def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains 
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    values.reverse()
    for value in values[::-1]: 
        for a in range(values.count(value) - 1): #leave 1 value behind
            values.remove(value)  
    values.reverse()
    