import unittest
from lab5 import gen_bin_tree
class TestTree(unittest.TestCase):
    def test_tree1(self):
        self.assertEqual(gen_bin_tree(height=3,root=16),{'root': 16, 'root.left': 8, 'root.right': 32, 'root.left.left': 4, 'root.left.right': 16, 'root.right.left': 16, 'root.right.right': 64})
    def test_tree2(self):
        self.assertEqual(gen_bin_tree(2, 12), {'root': 12, 'root.left': 6, 'root.right': 24})
    def test_tree3(self):
        self.assertEqual(gen_bin_tree(1, 15), {'root': 15})
    def test_tree4(self):
        self.assertEqual(gen_bin_tree(0, 12), {})
    def test_tree5(self):
        self.assertEqual(gen_bin_tree(-16, 4), "Высота дерева должна быть неотрицательна")