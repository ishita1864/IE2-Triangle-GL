import unittest
from isTriangle import Triangle

class TestStatementCoverage(unittest.TestCase):

    def test_statement_coverage(self):
        # Test case 1: Scalene triangle
        result = Triangle.classify(4, 5, 6)
        self.assertEqual(result, Triangle.Type.SCALENE)

        # Test case 2: Equilateral triangle
        result = Triangle.classify(8, 8, 8)
        self.assertEqual(result, Triangle.Type.EQUILATERAL)

        # Test case 3: Isosceles triangle
        result = Triangle.classify(5, 5, 3)
        self.assertEqual(result, Triangle.Type.ISOSCELES)
        
        # Test case 4: Isosceles triangle
        result = Triangle.classify(3,5, 5)
        self.assertEqual(result, Triangle.Type.ISOSCELES)
        
        # Test case 5: Isosceles triangle
        result = Triangle.classify(7, 5, 7)
        self.assertEqual(result, Triangle.Type.ISOSCELES)

        # Test case 6: Invalid triangle (one side is zero)
        result = Triangle.classify(0, 4, 5)
        self.assertEqual(result, Triangle.Type.INVALID)
        
        # Test case 7: Invalid triangle (2 side is zero)
        result = Triangle.classify(0, 0, 5)
        self.assertEqual(result, Triangle.Type.INVALID)


        # Test case 8: Invalid triangle (sum of two sides is less than the third side)
        result = Triangle.classify(1, 1, 3)
        self.assertEqual(result, Triangle.Type.INVALID)
        
        # Test case 9: Invalid triangle (sum of two sides is less than the third side)
        result = Triangle.classify(1, 2, 3)
        self.assertEqual(result, Triangle.Type.INVALID)
        
#         # Test case 5: Invalid triangle (sum of two sides is less than the third side)
#         result = Triangle.classify(0, 0, 0)
#         self.assertEqual(result, Triangle.Type.INVALID)
        
        
        
if __name__ == '__main__':
    unittest.main()

    