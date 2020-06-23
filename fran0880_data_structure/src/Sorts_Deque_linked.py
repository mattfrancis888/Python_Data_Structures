'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-04-03"
-------------------------------------------------------
'''

from math import log
from Deque_linked import Deque


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of linked sort operations.
    Uses class attribute 'swaps' to determine how many times 
    elements are swapped by the class.
    Use: print(Sorts.swaps)
    Use: Sorts.swaps = 0
    -------------------------------------------------------
    """
    swaps = 0  # Tracks swaps performed.

    # The Sorts

    @staticmethod
    def gnome_sort(a):
        """
        -------------------------------------------------------
        Sorts a Deque using the Gnome Sort algorithm.
        Use: gnome_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked structure of comparable elements (Deque)
        Returns:
            None
        -------------------------------------------------------
        """

        gnome_pos = a._front._next
        while gnome_pos:
            if gnome_pos._value < gnome_pos._prev._value:
                a._swap(gnome_pos, gnome_pos._prev)
                if gnome_pos == a._front: gnome_pos = gnome_pos._next
                
            else:
                gnome_pos = gnome_pos._next
        return

        return

    # Sort Utilities

    @staticmethod
    def sort_test(a):
        """
        -------------------------------------------------------
        Determines whether a linked deque is sorted or not.
        Use: sort_test(a)
        -------------------------------------------------------
        Parameters:
            a - a linked deque of comparable elements (?)
        Returns:
            returns
            is_sorted - True if contents of a are sorted, False otherwise.
        -------------------------------------------------------
        """
        is_sorted = True
        # Test forward links
        current = a._front

        while is_sorted and current is not None and \
                current._next is not None:

            if current._value <= current._next._value:
                current = current._next
            else:
                is_sorted = False
        # Test reverse links
        current = a._rear

        while is_sorted and current is not None and \
                current._prev is not None:

            if current._value >= current._prev._value:
                current = current._prev
            else:
                is_sorted = False

        return is_sorted