'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-03-27"
-------------------------------------------------------
'''
from Word import Word
def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in fv and inserts into
    a Hash_Set.
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        Each Word object in hash_set contains the number of comparisons
        required to insert that Word object from file_variable into hash_set.
    -------------------------------------------------------
    """
    fv.seek(0)
    words = []
    line = fv.readline()
    while line != "":
        line = fv.readline()
        for word in line.split():
            if word.isalpha() is True:
                words.append(word.lower())
                
    for i in range(len(words)):
        hash_set.insert(words[i])
        
def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    total = 0 
    max_word = Word('hi') #0 comparisons
    for word in hash_set:
        total += word.comparisons
        if word.comparisons > max_word.comparisons:
            max_word = word    
    return total, max_word
