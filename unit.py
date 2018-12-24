import unittest


def ExponentCalc(x, y):
    return x ** y

class ExponentCalcTest(unittest.TestCase):
    def testSuccess(self):
        result = ExponentCalc(5,4)
        self.assertEqual(result, 625)

    def testFailure(self):
        result = ExponentCalc(3,8)
        self.assertNotEqual(result, 6560)

#print(ExponentCalc(5,4))

unittest.main()

