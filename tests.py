import unittest
from goog4_2 import Graph, gcd, game

class TestGoog(unittest.TestCase):

    def testgcd(self):
        self.assertEqual(gcd(8,12), 4)
        self.assertEqual(gcd(13,7), 1)
        self.assertEqual(gcd(25,10), 5)
        self.assertEqual(gcd(4,23), 1)
        self.assertEqual(gcd(7,26), 1)
        self.assertEqual(gcd(36,24), 12)
        self.assertEqual(gcd(49, 14), 7)
    
    def testgame(self):
        self.assertTrue(game(13,1))
        self.assertFalse(game(1,7))
        self.assertFalse(game(1,3))
        self.assertFalse(game(1,15))
        self.assertFalse(game(19,13))
        self.assertFalse(game(7,21))
        self.assertFalse(game(1,1073741823))
        self.assertTrue(game(23,36))

    def testgraph(self):
        A = Graph([1,1])
        B = Graph([1,7,3,19,21,13])
        C = Graph([2,5,9,22,31,47,25,26])
        D = Graph([1,1073741823, 7, 153391689])
        Cg = [[0,1,1,1,1,1,1,1],
              [1,0,1,1,1,1,1,1],
              [1,1,0,1,1,1,1,1],
              [1,1,1,0,1,1,1,1],
              [1,1,1,1,0,1,1,1],
              [1,1,1,1,1,0,1,1],
              [1,1,1,1,1,1,0,1],
              [1,1,1,1,1,1,1,0]]
        Dg = [[0,0,0,1],
              [0,0,1,0],
              [0,1,0,1],
              [1,0,1,0]]
        self.assertEqual(A.length, 2)
        self.assertEqual(B.length, 6)
        self.assertEqual(A.graph, [[0,0],[0,0]])
        self.assertEqual(B.graph, [ [0, 0, 0, 1, 1, 1], 
                                    [0, 0, 1, 1, 0, 1], 
                                    [0, 1, 0, 1, 0, 0], 
                                    [1, 1, 1, 0, 1, 0], 
                                    [1, 0, 0, 1, 0, 1], 
                                    [1, 1, 0, 0, 1, 0]])
        self.assertEqual(C.graph, Cg)
        self.assertEqual(D.graph, Dg)
if __name__ =='__main__':
    unittest.main()