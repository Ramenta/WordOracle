import unittest
from DictionaryOrg import OnlineDictionary


class Test(unittest.TestCase):
    def setUp(self):
        self.dictionary = OnlineDictionary()


    def tearDown(self):
        pass


    def testFail(self):
        self.assertTrue(False, "This test is intentionally failing")


if __name__ == "__main__":
    unittest.main()