'''
Node class
'''

class Node: 
    # Constructor to create a new node 
    def __init__(self, data): 
        self.val = data 
        self.left = None
        self.right = None
        
    def getVal(self):
        return self.val