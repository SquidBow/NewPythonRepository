import os
import pandas.testing as test
import pandas
import unittest


def testFileWritePandas1():
    with open ("test.txt", 'w') as file:
        file.write("age,name\n41,Max\n25,Teodor")

    result = pandas.read_csv("test.txt")

    expected = pandas.DataFrame({
        "age": [41, 25],
        "name": ["Max", "Teodor"],
    })

    os.remove("test.txt")

    test.assert_frame_equal(result, expected)

class TestPandas(unittest.TestCase):
    def testFileWritePandas3(self):
        with self.assertRaises(FileNotFoundError):
            pandas.read_csv("test.txt")

    def testFileWritePandas2(self):
        with open("test.txt", 'w'):
            pass

        with self.assertRaises(pandas.errors.EmptyDataError):
            pandas.read_csv("test.txt")

        os.remove("test.txt")


def testFileWrite1():
    with open ("test.txt", 'w') as file:
        pass

    with open("test.txt", 'r') as file:
        result = file.read()

    os.remove("test.txt")

    assert result == ""

class TestFile(unittest.TestCase):
    def testFileWrite3(self):
        with self.assertRaises(FileNotFoundError):
            with open("test.txt", 'r') as file:
                file.read()

def testFileWrite2():
    with open ("test.txt", 'w') as file:
        file.write("age,name\nMax,41\nTeodor,25")

    with open("test.txt", 'r') as file:
        result = file.read()

    os.remove("test.txt")

    assert result == "age,name\nMax,41\nTeodor,25"
