'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-01-28"
-------------------------------------------------------
'''
from Stack_array import Stack


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    stack_list = []
    while not source.is_empty():
        stack_list.append(source.pop())
    for val in stack_list:
        source.push(val)
        

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack. 
    When finished, the contents of source1 and source2 are interlaced 
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    while not source1.is_empty() or not source2.is_empty():
        if source1.is_empty():
            target.push(source2.pop())
        elif source2.is_empty():
            target.push(source1.pop())
        else:
            #if both sources are full
            target.push(source1.pop())
            target.push(source2.pop())    
    return target
def combine(self, source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into the current target stack. 
    When finished, the contents of source1 and source2 are interlaced 
    into target and source1 and source2 are empty.
    Use: target.combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - an array-based stack (Stack)
        source2 - an array-based stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    
# Constants
BALANCED = 0
MORE_LEFT = 1
MORE_RIGHT = 2
MISMATCHED = 3

def has_balanced_brackets(string):
    """
    -------------------------------------------------------
    Determines if a string contains balanced brackets or not. Non-bracket
    characters are ignored. Uses a stack. Brackets include {}, [], (), <>.
    Use: balanced = has_balanced_brackets(string)
    -------------------------------------------------------
    Parameters:
        string - the string to test (str)
    Returns:
        balanced (int) -
            BALANCED if the brackets in string are balanced
            MISMATCHED if the brackets in string are mismatched
            MORE_RIGHT if there are more right brackets than left in string
            MORE_LEFT if there are more left brackets than right in string
    -------------------------------------------------------
    """

    left_brackets = ["{", "[", "(", "<"]
    right_brackets = ["}", "]", ")", ">"]
    brace_dict = {"{":"}", "[":"]", "(":")", "<":">"}
    
    s = Stack()
    
    left = 0
    right = 0
    
    balanced = True
    
    for bracket in string:
        
        if bracket in left_brackets:
            s.push(bracket)
            left += 1
        elif bracket in right_brackets:
            right += 1
            
            if s.is_empty():
                #If no left bracket
                balanced = False
            
            elif not brace_dict[s.pop()] == bracket:
                #if left bracket does not match right bracket
                balanced = False
                
    if not s.is_empty():
        # more left brackets then closing right brackets
        balanced = False
        
    if not balanced:
        if right == left:
            return MISMATCHED
        elif right > left:
            return MORE_RIGHT
        else:
            return MORE_LEFT
    else:
        return BALANCED

# Constants
OPERATORS = "+-*/"

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    s = Stack()
    
    answer = 0
    string = string.strip().split(' ')
    for val in string:
        if val.isdigit():
            val = int(val)
            s.push(val)
            
        elif val in OPERATORS:
            assert not s.is_empty() , 'Stack is empty , must have 2 values' # MUST HAVE 2 VALUES IN STACK
            a = s.pop()
            assert not s.is_empty(), 'Stack is empty, must have 1 more value'
            b = s.pop() # can pose a problem if there is only 1 item in stack
            if val == '+':
                #top in stack is to the right
                answer = b + a 
                #bottom in stack is to the left
                print('{:d} + {:d}'.format(b,a))
            elif val == '-':
                answer = b - a
                print('{:d} - {:d}'.format(b,a))
            elif val == '*':
                answer = b * a
                print('{:d} * {:d}'.format(b,a))
            elif val == '/':
                answer = b / a
                print('{:d} / {:d}'.format(b,a))
                
            print('TOTAL:', answer)
            s.push(answer)
    return answer 
    
def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    
    palindrome = True
    even = False
    s = Stack()
    index = 0
    temp_string = ""
    
    for char in string:
        #ignore anything that is not an alphabet or a number
        if char.isalpha() or char.isdigit():
            temp_string += char.lower()
    
    if len(temp_string) % 2 == 0:
        even = True
   
    mid_index = len(temp_string) // 2 # round down
    #ex; 3 words abc; mid_index is 1
    
    for char in temp_string:
        #stop in the middle of the word
        if index < mid_index:
            s.push(char)
            
        #if even and after reaching mid point   
        elif even:
            if char != s.pop():
                palindrome = False
                return palindrome
            
        #if not even and after reaching mid point
        elif even is False and index > mid_index:
            if char != s.pop():
                palindrome = False
                return palindrome  
                    
        index += 1
    return palindrome
