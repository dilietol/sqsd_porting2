import unittest
from sqssender import SqsSender

sqssender = SqsSender()


class TestSqsSender(unittest.TestCase):

    def test_send(self):
        self.assertEqual(sqssender.send("Test Message"), 200)

    def test_sendMultiplo(self):
        x = range(100)
        for n in x:
            self.assertEqual(sqssender.send("Test Message"), 200)


if __name__ == '__main__':
    unittest.main()
