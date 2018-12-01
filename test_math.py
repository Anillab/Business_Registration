import unittest
import maths

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(maths.add(2,4),6)
        self.assertEqual(maths.add(-2,-4),-6)
        self.assertEqual(maths.add(2,-4),-2)
if __name__ == '__main__':
    unittest.main()
