'''
Traversal class includes seversal traversal methods: inorder, preorder, postorder
'''
from src.node import Node
from typing import List

class Traversal:       
    
    """ Recursive method """
    def InOrderTraversal_Recursive(self, root: Node) -> List:
        ans = [] 
        def innerecursion(root, ans):
            if not root:
                return
            innerecursion(root.left, ans)
            ans.append(root.val)
            innerecursion(root.right, ans)
    
        innerecursion(root, ans)
        return ans
    
    
    """ Iterative method """
    def InOrderTraversal_Iterative(self, root: Node) -> List:
        ans = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            ans.append(node.val)
            root = node.right
        return ans
    
    """ Recursive method """
    def PreOrderTraversal_Recursive(self, root: Node) -> List:
        ans = [] 
        def innerecursion(root, ans):
            if not root:
                return
            ans.append(root.val)
            innerecursion(root.left, ans)
            innerecursion(root.right, ans)
    
        innerecursion(root, ans)
        return ans


    """ Iterative method """
    def PreOrderTraversal_Iterative(self, root: Node) -> List:
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans
    
    """ Recursive method """
    def PostOrderTraversal_Recursive(self, root: Node) -> List:
        ans = [] 
        def innerecursion(root: Node, ans: List) -> List:
            if not root:
                return
            innerecursion(root.left, ans)
            innerecursion(root.right, ans)
            ans.append(root.val)
    
        innerecursion(root, ans)
        return ans

    """ Iterative method """
    def PostOrderTraversal_Iterative(self, root: Node) -> List:
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                ans.append(node.val)
        return ans[::-1]