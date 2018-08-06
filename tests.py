import unittest
from goog4_2 import power, between, isSpecial, Graph, make_graph, gcd

class TestGoog(unittest.TestCase):

    def testpower(self):
        self.assertTrue(power(1))
        self.assertTrue(power(3))
        self.assertTrue(power(7))
        self.assertTrue(power(15))
        self.assertTrue(power(31))
        self.assertTrue(power(63))
        self.assertFalse(power(2))
        self.assertFalse(power(4))
        self.assertFalse(power(8))
        self.assertFalse(power(16))

    def testzetween(self):
        self.assertFalse(between(1,1))
        self.assertTrue(between(1,2))
        self.assertFalse(between(1,3))
        self.assertTrue(between(1,4))
        self.assertTrue(between(1,5))
        self.assertTrue(between(1,6))
        self.assertFalse(between(1,7))
        self.assertFalse(between(1,15))
        self.assertTrue(between(2,5))
        self.assertFalse(between(2,6))
        self.assertFalse(between(2,30))
        self.assertTrue(between(2, 8))
        self.assertFalse(between(500, 127500))
        self.assertFalse(between(1,1073741823))

    def testcheck(self):
        self.assertTrue(isSpecial(13, 3))
        self.assertTrue(isSpecial(25, 7))
        self.assertTrue(isSpecial(57, 7))
        self.assertTrue(isSpecial(9, 7))
        self.assertTrue(isSpecial(5, 3))
        self.assertTrue(isSpecial(17,15))

    def testgraph(self):
        A = Graph([1,1])
        B = Graph([1,7,3,19,21,13])
        C = make_graph([1,1])
        D = make_graph([1,7,3,19,21,13])
        print(A.graph)
        print(gcd(64,16))
        print(C)
        print(B.graph)
        print(D)
        self.assertEqual(A.length, 2)
        self.assertEqual(B.length, 6)

if __name__ =='__main__':
    unittest.main()