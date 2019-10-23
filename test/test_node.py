'''
pytest example on Node class
'''

from src.node import Node
import pytest

class TestNode:
    def test_getVal(self):
        root = Node(5)
        expected = 5
        
        assert expected == root.getVal(), "getVal fails"