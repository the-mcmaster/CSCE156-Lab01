import unittest

from statistics import sumVals
from statistics import maximum

class StatisticsUnitTests(unittest.TestCase):

    testCases = [
        ([1, 2, 3, 4], 10),
        ([-1, -2, -3, -4], -10)
    ]

    def test_batchTest(self):
        """This is a batch test that tests multiple input/output
        pairs as defined in the testCases (a list of pairs/tuples).
        However, it only counts as *one* test.  If any one of the
        input/output combinations fails, the entire test fails.
        Generally, tests should be smaller like the test cases below.
        """
        for (testVals,expectedOutput) in self.testCases:
            actualOutput = sumVals(testVals)
            self.assertEqual(expectedOutput,actualOutput)

    # all unit tests begin with "test"
    def test_sumVals_001(self):
        testVals = [1, 2, 3]
        expectedOutput = 6
        actualOutput = sumVals(testVals)
        self.assertEqual(expectedOutput, actualOutput)

    def test_sumVals_002(self):
        testVals = [1, 6, 2, 7, 3, 8, 4, 9, 5, 10]
        expectedOutput = 55
        actualOutput = sumVals(testVals)
        self.assertEqual(expectedOutput, actualOutput)

    def test_sumVals_003(self):
        testVals = [-4, 3, -42, 21, 0, 3, 3, 3, 3]
        expectedOutput = -10
        actualOutput = sumVals(testVals)
        self.assertEqual(expectedOutput, actualOutput)

    def test_sumVals_004(self):
        testVals = [-1, -2, -3, -4, -5]
        expectedOutput = -15
        actualOutput = sumVals(testVals)
        self.assertEqual(expectedOutput, actualOutput)

    def test_sumVals_005(self):
        testVals = [-1, -2, 3, 2, -3, 1]
        expectedOutput = 0
        actualOutput = sumVals(testVals)
        self.assertEqual(expectedOutput, actualOutput)

    def test_maximum_001(self):
        testVals = [1, 2, 3]
        expectedOutput = 3
        actualOutput = maximum(testVals)
        self.assertEqual(expectedOutput, actualOutput)

    def test_maximum_002(self):
        testVals = [1, 6, 2, 7, 3, 8, 4, 9, 5, 10]
        expectedOutput = 10
        actualOutput = maximum(testVals)
        self.assertEqual(expectedOutput, actualOutput)

    def test_maximum_003(self):
        testVals = [-4, 3, -42, 21, 0, 3, 3, 3, 3]
        expectedOutput = 21
        actualOutput = maximum(testVals)
        self.assertEqual(expectedOutput, actualOutput)

    def test_maximum_004(self):
        testVals = [-1, -2, -3, -4, -5]
        expectedOutput = -1
        actualOutput = maximum(testVals)
        self.assertEqual(expectedOutput, actualOutput)

    def test_maximum_005(self):
        testVals = [-1, -2, 3, 2, -3, 1]
        expectedOutput = 3
        actualOutput = maximum(testVals)
        self.assertEqual(expectedOutput, actualOutput)

if __name__ == '__main__':
    unittest.main()