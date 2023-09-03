from __future__ import print_function
import unittest
import os


class TestExample(unittest.TestCase):
    def setUp(self):
        self.test_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "..", "data")

    def test_example(self):
        from example import example_function
        import numpy as np

        # array of 100 random int32 numbers
        a1 = np.random.randint(0, 100, 100).astype(np.int32)
        a2 = np.random.randint(0, 100, 100).astype(np.int32)
        b1, b2 = example_function(a1, a2)
        self.assertTrue(np.all(a1 == b1))
        self.assertTrue(np.all(a2 == b2))

        # array of 100 random int64 numbers
        a1 = np.random.randint(0, 100, 100).astype(np.int64)
        a2 = np.random.randint(0, 100, 100).astype(np.int64)
        b1, b2 = example_function(a1, a2)
        self.assertTrue(np.all(a1 == b1))
        self.assertTrue(np.all(a2 == b2))

        for dtype_str in ["intc", "int", "long", "longlong"]:
            a1 = np.random.randint(0, 100, 100,dtype=dtype_str)
            a2 = np.random.randint(0, 100, 100,dtype=dtype_str)
            b1, b2 = example_function(a1, a2)
            self.assertTrue(np.all(a1 == b1))
            self.assertTrue(np.all(a2 == b2))



if __name__ == '__main__':
    unittest.main()
