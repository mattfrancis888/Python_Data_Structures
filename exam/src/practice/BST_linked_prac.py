'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-04-11"
-------------------------------------------------------
'''
from platform import node
"""
-------------------------------------------------------
Linked version of the BST ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2018-11-14"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers 
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns:
            A _BST_Node object (_BST_Node)            
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        self._count = 0

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Returns:
            _height is 1 plus the maximum of the node's two children.
        -------------------------------------------------------
        """
        # your code here
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height
        
        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height
        
        self._height = max(left_height, right_height) + 1
        return self._height

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into the bst (?)
        Returns:
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        # Need to track when node is traversing and insert a value, so create aux
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted
       
    def _insert_aux(self, node, value):
            
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        #Goal: Keep iterating trough tree until you find a
        #proper spot for value
        if node is None:
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif node._value > value:
            #Move to left subtree
            node._left, inserted = self._insert_aux(node._left, value)
        elif node._value < value:
            #Move right subtree
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            inserted = False
            
        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted
        

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None
        while node is not None and value is None:
            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                value = deepcopy(node._value)
        
        return value
        # your code here
        return

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched. Updates structure of bst as 
        required.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value matching key if found, otherwise None.
        -------------------------------------------------------
        """
        # your code here
        return

    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Parameters:
            parent - node to search for largest value (_BST_Node)
        Returns:
            repl_node - the node that replaces the deleted node. This node 
                is the node with the maximum value in the deleted node's left
                subtree (_BST_Node)
        -------------------------------------------------------
        """
        # your code here
        return

    def remove_root(self):
        """
        -------------------------------------------------------
        Removes the root node and returns its value.
        Use: value = bst._remove_root()
        -------------------------------------------------------
        Returns:
            value - value in root.
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot remove the room of an empty BST"

        # your code here
        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the bst contains key.
        Use: b = key in bst
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the bst contains key, False otherwise.
        -------------------------------------------------------
        """
        value = self.retrieve(key)
        return value is not None

    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a BST, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Returns:
            maximum height of bst (int)
        -------------------------------------------------------
        """
        if self._root is None:
            h = 0
        else:
            h = self._root._height
        return h

    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are identical.
        Use: b = bst.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another bst (BST)
        Returns:
            identical - True if this bst contains the same values
            in the same order as other, otherwise returns False (boolean)
        -------------------------------------------------------
        """
        #Need to compare self BST and other BST, so create an aux
        if self._count != other._count:
            identical = False
        else:
            identical = self._is_identical_aux(self._root, other._root)
        
        
        return identical

    def _is_identical_aux(self, node1, node2):
        """
        ---------------------------------------------------------
        Determines whether two subtrees are identical.
        Use: b = self._is_identical_aux(node1, node2)
        -------------------------------------------------------
        Parameters:
            node1 - node of the current BST (_BST_Node)
            node2 - node of the rs BST (_BST_Node)
        Returns:
            identical - True if this subtree contains the same values as rs
                subtree in the same order, otherwise returns False (boolean)
        -------------------------------------------------------
        """
        #Need to make sure node exist, value and height are the same!
        
        if node1 is None and node2 is None:
            #Base case: Reached a bottom of the tree.
            identical = True
            
        elif node1 is not None and node2 is not None \
                and node1._value == node2._value and node1._height == node2._height:
            
            identical = self._is_identical_aux(node1._left, node2._left) \
                and self._is_identical_aux(node1._right, node2._right)
       
        else:
            identical = False
        return identical

    def parent_i(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found. (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"
        node = self._root
        parent = None
        found = False
        
        while node is not None and found is False:
            if key < node._value:
                parent = node
                node = node._left
            elif key > node._value:
                parent = node
                node = node._right
            else:
                #parent is already assigned 
                found = True
        
        if parent is None or not found:
            value = None
        else:
            value = deepcopy(parent._value)
        return value

    def parent_r(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node in a bst given a key.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"
        #Need to keep track of parent and node, so  create an aux
        value = self._parent_aux(self._root, key, None)
        return value
    def _parent_aux(self, node, key, parent):
        """
        ---------------------------------------------------------
        Returns the _value of the parent node in a bst given a _value.
        Private recursive operation called only by parent_r.
        Use: v = self._parent_aux(node, key, parent of node)
        ---------------------------------------------------------
        Parameters:
            node - a BST node
            key - a key _value
            parent - the parent node of the current node
        Returns:
            value - the value of the parent node, None if it has no parent (?)
        ---------------------------------------------------------
        """
        
        if node is None:
            #Empty BST or can't find key
            value = None
        elif key < node._value:
            value = self._parent_aux(node._left, key, node)
        elif key > node._value:
            value = self._parent_aux(node._right, key, node)
        else:
            #key == node._value
            value = parent._value
        return value
    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"
        
        node = self._root
        while node._right is not None:
            node = node._right
        value = deepcopy(node._value)
        return value

    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        value = self._max_aux(self._root)
        return value
    def _max_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the largest value in a BST node. (Recursive algorithm)
        Use: v = self._max_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - is_valid linked BST node (_BST_Node)
        Returns:
            value - a copy of the largest value in the node subtree (?)
        ---------------------------------------------------------
        """
        if node._right is None:
            #Base case: reached the end
            value = deepcopy(node._value)
        else:
            value = self._max_aux(node._right)
        return value
    
    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in BST. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"
        node = self._root

        while node._left is not None:
            node = node._left

        value = deepcopy(node._value)
        return value

    def min_r(self):
        """
        ---------------------------------------------------------
        Returns the minimum value in a bst. (Recursive algorithm)
        Use: value = bst.min_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        value = self._min_aux(self._root)
        return value

    def _min_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the minimum value in a BST node. (Recursive algorithm)
        Use: v = self._max_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - is_valid linked BST node (_BST_Node)
        Returns:
            value - a copy of the minimum value in the node subtree (?)
        ---------------------------------------------------------
        """
        if node._left is None:
            value = deepcopy(node._value)
        else:
            value = self._min_aux(node._left)
        return value
    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: n = bst.leaf_count()
        (Recursive algorithm)
        ---------------------------------------------------------
        Returns:
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """
        # Need to traverse nodes so create an aux
        count = self._leaf_count_aux(self._root)
        return count
    def _leaf_count_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: count = bst.leaf_count()
        ---------------------------------------------------------
        Parameters:
            node - a BST node (_BST_Node)
        Returns:
            count - number of nodes with no children below node (int)
        ---------------------------------------------------------
        """
        #think of both recursion calls as one recursion call
        if node is None:
            #Base case: node is empty
            count = 0 
        elif node._left is None and node._right is None:
            #Base case: node has no children
            #Saying: add a count, done traversing.
            count = 1
        else:
            #General case: Keep traversing
            count = self._leaf_count_aux(node._left) + \
                self._leaf_count_aux(node._right)
        return count
        

    def two_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.two_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """
        # your code here
        return self._two_child_count_aux(self._root)

    def _two_child_count_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of types of nodes in a BST node.
        -------------------------------------------------------
        Parameters:
            node - a BST node (_BST_Node)
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """
        if node is None:
            # Base case: node is empty.
            count = 0
        elif node._left is not None and node._right is not None:
            # General case: node has two children.
            
            #Saying: Add 1, traverse again, get all the count
            #values from the recursive call and add it up to count
            count = 1 + self._two_child_count_aux(node._left) + \
                self._two_child_count_aux(node._right)
        else:
            # General case: node has one child.
            count = self._two_child_count_aux(node._left) + \
                self._two_child_count_aux(node._right)
        return count
    def one_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.one_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with one child in bst (int)
        ----------------------------------------------------------
        """
        # your code here
        return

    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Returns:
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """
        zero, one, two = self._node_counts_aux(self._root)
        return zero, one, two

    def _node_counts_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of types of nodes in a BST node.
        -------------------------------------------------------
        Parameters:
            node - a BST node (_BST_Node)
        Returns:
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """
        if node is None:
            # Base case: no node.
            one = 0
            two = 0
            zero = 0
        elif node._left is None and node._right is None:
            # Base case: node has no children.
            one = 0
            two = 0
            zero = 1
        elif node._left is not None and node._right is None:
            # General case: node has a single left child.
            zero, one, two = self._node_counts_aux(node._left)
            one += 1
        elif node._left is None and node._right is not None:
            # General case: node has a single right child.
            zero, one, two = self._node_counts_aux(node._right)
            one += 1
        
#         Technicaly...the 2 above if statements can be combined with
#             an or statement...and then, below it:

#             zero, one, two, = self._two_child_count_aux(node._left) + \
#                 self._two_child_count_aux(node._right)
#             one += 1
#             ? We did this for two_counts.
        
        else:
            # General case: node has two children. Get node counts
            # from both children.
            zero_l, one_l, two_l = self._node_counts_aux(node._left)
            zero_r, one_r, two_r = self._node_counts_aux(node._right)
            zero = zero_l + zero_r
            one = one_l + one_r
            # Count the current node as one with two children.
            two = two_l + two_r + 1
        return zero, one, two
    def is_balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.is_balanced()
        ---------------------------------------------------------
        Returns:
            balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        balanced = self._is_balanced_aux(self._root)
        return balanced

    def _is_balanced_aux(self, node):
        """
        ---------------------------------------------------------
        Determines whether the BST is is_balanced.
        Private operation called only by _is_valid_aux.
        Use: b = self._balanced_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to check the balance of (_BST_Node)
        Returns:
            balanced - True if node is is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if node is None or node._height == 1:
            #node._height if self._root is the only node
            # Base case: node is empty or a leaf, so no children.
            balanced = True
        elif abs(self._node_height(node._left) -
                 self._node_height(node._right)) > 1:
            # Base case: left or right subtree is too deep.
            balanced = False
        else:
            # General case: check the children of node.
            balanced = self._is_balanced_aux(node._left) and \
                self._is_balanced_aux(node._right)
        return balanced
    
    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height
    def retrieve_r(self, key):
        """
        -------------------------------------------------------
        Retrieves a _value in a BST. (Recursive)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - If bst contains key, returns value, else returns None.
        -------------------------------------------------------
        """
        # your code here
        return

    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a is_valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        valid = self._is_valid_aux(self._root)
        return valid

    def _is_valid_aux(self, node):
    
        if node is None:
            return True
        #must be false conditions!
        elif node._left is not None and node._left._value > node._value or node._right is not None and node._right._value < node._value :
            return False
        #height
        elif node._left is not None and node._left._height > node._height or node._right is not None and node._right._height > node._height:
            return False
        else:
            return self._is_valid_aux(node._left) and self._is_valid_aux(node._right)

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        # your code here
        return

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        # your code here
        return

    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        # your code here
        return

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        # your code here
        return

    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Returns:
            number - count of nodes in tree (int)
        ----------------------------------------------------------
        """
        # your code here
        return

    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns:
            yields
            value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)