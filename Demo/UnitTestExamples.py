import unittest
from Examples import Example


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("This will run before every mehtod ")

    def tearDown(self):
        print("This will run after every mehtod ")
    def test_add(self):
        result=Example.add(self,10,20)
        self.assertEqual(result,30)

    def test_sub(self):
        result=Example.sub(self,50,30)
        self.assertEqual(result,20)

    def test_add_1(self):
        self.assertEqual(Example.add(self,10,40),50)
        self.assertEqual(Example.add(self,100,100),200)

if __name__ == '__main__':
    unittest.main()
