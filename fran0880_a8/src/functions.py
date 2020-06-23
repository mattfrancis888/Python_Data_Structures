'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-03-20"
-------------------------------------------------------
'''
from Letter import Letter
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"


def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains 
    the number of comparisons found by searching for that Letter 
    object in file_variable.
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects 
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    file_variable.seek(0)

    for line in file_variable:

        for char in line.strip():
            if char.isalpha():
                #what is l
                l = Letter(char.upper())
                bst.retrieve(l)
    return


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    a = bst.inorder()

    for v in a:
        total = total + v.comparisons
    return total


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts.
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    t_c = 0
    a = bst.inorder()

    for i in a:
        t_c += i.count
    print("Letter Count/Percent Table")
    print()
    print("Total Count: {:,}".format(t_c))
    print()
    print("Letter  Count          %")
    print("------------------------")
    for i in a:
        print("{:>2}{:9,d}{:>13.2%}".format(i.letter, i.count, i.count / t_c))
    return