import strings
import Triangle_Classifier
import unittest

################################################################################
class Triangle_Clasifier_unittests(unittest.TestCase):

    def setUp(self):
        self.testfile = open("fixtures.txt", "r")

    def tests(self):
        test_cases = []
        for line in self.testfile:
            line = line.strip()
            list = line.split(',')
            test_cases.append(list)

        for input, expected in test_cases:
            with self.subTest(input=input, expected=expected):
                print(f"[TEST] {input} : {expected}")
                result = Triangle_Classifier.Get_Triangle_Type(input).upper()
                self.assertEqual(result, expected.upper())

    def tearDown(self):
        print("CLOSING FILE")
        self.testfile.close()
################################################################################

################################################################################
if __name__ == '__main__':
    unittest.main()
################################################################################