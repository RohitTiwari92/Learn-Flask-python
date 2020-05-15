import unittest
import getquckUnioncodeDC
import getquckfindcodeDC

class testclass(unittest.TestCase):
    def test_qu(self):
        data=getquckUnioncodeDC.getquckUnioncodeDC()
        self.assertIsNotNone(data)


if __name__ == '__main__':
    unittest.main()

