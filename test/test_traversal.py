'''
pytest example on Binary Tree Traversal
'''

from src.traversal import Traversal
from src.node import Node
import pytest


"""
generate testing data

"""
def generateBinaryTree():
    root = Node(10) 
    root.left = Node(6) 
    root.right = Node(15) 
    root.left.left = Node(5) 
    root.left.right = Node(7) 
    root.right.left = Node(12)
    root.right.right = Node(18)
    return root


class TestTraversal:
    def test_InOrderTraversal_Recursive(self):
        sol = Traversal()
        root = generateBinaryTree()
        result = sol.InOrderTraversal_Recursive(root)
        expected = [5,6,7,10,12,15,18]
        assert result == expected, "test fails on inorder recursive method"
        
    def test_InOrderTraversal_Iterative(self):
        sol = Traversal()
        root = generateBinaryTree()
        result = sol.InOrderTraversal_Iterative(root)
        expected = [5,6,7,10,12,15,18]
        assert result == expected, "test fails on inorder iterative method"
        
    def test_PreOrderTraversal_Recursive(self):
        sol = Traversal()
        root = generateBinaryTree()
        result = sol.PreOrderTraversal_Recursive(root)
        expected = [10,6,5,7,15,12,18]
        assert result == expected, "test fails on preorder recursive method"
        
    def test_PreOrderTraversal_Iterative(self):
        sol = Traversal()
        root = generateBinaryTree()
        result = sol.PreOrderTraversal_Iterative(root)
        expected = [10,6,5,7,15,12,18]
        assert result == expected, "test fails on preorder iterative method"
        
    def test_PostOrderTraversal_Recursive(self):
        sol = Traversal()
        root = generateBinaryTree()
        result = sol.PostOrderTraversal_Recursive(root)
        expected = [5,7,6,12,18,15,10]
        assert result == expected, "test fails on postorder recursive method"
        
    def test_PostOrderTraversal_Iterative(self):
        sol = Traversal()
        root = generateBinaryTree()
        result = sol.PostOrderTraversal_Iterative(root)
        expected = [5,7,6,12,18,15,10]
        assert result == expected, "test fails on postorder iterative method"
