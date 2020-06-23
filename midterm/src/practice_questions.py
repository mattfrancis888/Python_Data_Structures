'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-02-12"
-------------------------------------------------------
'''
from Stack_array import Stack
def low_cal(foods, count):
    """
    -------------------------------------------------------
    Returns a list of foods with a calorie count less than count.
    Use: low_cal_foods = low_cal(foods, count)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        count - foods must have calories below count (int)
    Returns:
        returns
        low_cal_foods - a list of Food (list of Food)
    -------------------------------------------------------
    """
    low_cal_foods = []
    for x in range(len(foods)):
        if foods[x]<count:    
            low_cal_foods.append(food[x])
    return low_cal_foods

def has_balanced_brackets(s):
    """
    -------------------------------------------------------
    Determines whether a string contains balanced brackets or not.
    Must use a Stack to do so.
    Use: b = balanced_brackets(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        balanced - True if s contains balanced brackets, False otherwise (boolean)
    -------------------------------------------------------
    """
    LEFT_B='[{(<'
    RIGHT_B='>)}]'
    balanced=False
    stack=Stack()
    
    for x in s:
        if x in LEFT_B:
            stack.push(x)
            
        elif x in RIGHT_B:
            if not stack.is_empty():
                balanced = False
                
            elif x != stack.pop():
                balanced = False
                
            else:
                balanced=True

    return balanced

    def postfix(s):
        """
        -------------------------------------------------------
        Evaluates a string as postfix expression.
        Must use a Stack to do so.
        Use: b = postfix(s)
        -------------------------------------------------------
        Parameters:
            s - a postfix expression in a string (str)
        Returns:
            result - the result of evaluating the postfix expression in s (float)
        -------------------------------------------------------
        """
        #12 5 -
        #becomes 12 - 5 = 7
    
        stack=Stack()
        OP='+, -, *, /'
        
        result =0
        for x in s.split(' '):
            if x.isdigit():
                stack.push(x)
            elif x in OP:
                a = stack.pop()
                b = stack.pop()
                if x=='+':
                    result = b + a
                elif x=='-':
                    result = b - a
                elif x=='*':
                    result =b * a
                else:
                    result=b /a
                stack.push(result)
        return result

def total_priority(pq):
    """
    -------------------------------------------------------
    Returns the total priority of all elements of a priority queue.
    Use: n = total_priority(pq)
    -------------------------------------------------------
    Parameters:
        pq - a priority queue with integer priorities (PriorityQueue)
    Returns:
        n - the sum of all priority values in pq (int)
    -------------------------------------------------------
    """
    while not pq.is_empty():
        n += pq.remove()
    return n


class Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Set.
        Use: s = Set()
        -------------------------------------------------------
        Returns:
            Initializes an empty set.
        -------------------------------------------------------
        """
        
        self._vales=[]
        
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the set is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Returns:
            True if the set is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the set.
        Use: n = len(s)
        -------------------------------------------------------
        Returns:
            the number of values in the set.
        -------------------------------------------------------
        """
        return len(self._values)

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the set.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of key in the set, -1 if key is not found (int)
        -------------------------------------------------------
        """
        
        check=True
        x=0
        i=-1
        while i < len(self._values) and check:
          if self._values[x]!=i:
            x+=1
          else:
            check=False
        return i

    def insert(self, i, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the set.
        Use: b = s.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            inserted - True if the value was inserted at i, False otherwise.
                value is inserted at position i or appended to the end of the set
                if i > len(s) only if value is unique in the set (boolean)
        -------------------------------------------------------
        """
#         if i > -1 and i < len(s)-1:
#            self._values =self._values[:i]+[deepcopy(value)]+self._values[i:]
#             inserted=True
#         else:
#             self._values.append(deepcopy(value))
#             inserted=False
        
#         return inserted
        inserted = False
        if value not in self._values:
            if i < len(self._values):
                self._values = self._values[:i] + [deepcopy(value)] + self._values[i:]
                inserted = True
            else:
                self._values = self._values[:] + deepcopy(value)
        return inserted


    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the set that matches key.
        Use: value = s.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        i = self._linear_search(key)
        
        if i != -1:
             value=self._values[i]    
             self._values.remove(value)
        else:
            value = None
        
        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in the set that matches key.
        Use: value = s.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot find in an empty set"
        i=self._linear_search(key)
        value=self._values[i]
        return value
        
    

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the set (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty set"
        
        value=deepcopy(self._values[0])
        
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of key in the set.
        Use: n = s.index( key )
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the location of the full value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """
        found = False
        i = 0
        
        while i < len(self._values) and not found:
            if self._values[i] == key:
                found = True
            i += 0 
        if found == False:
            i= -1
            
        return i


    def _valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(set) to len(set) - 1
        Use: assert self._valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = len(self._values)
        return -n <= i < n