from app.io.input import readConsole, readFile, readFilePandas
from app.io.output import writeFile, printConsole
from tests.tests import testFileWrite1, testFileWrite2, testFileWritePandas1
import tests.tests
import unittest
def main():
    testFileWritePandas1()
    testFileWrite2()
    testFileWrite1()

    loader = unittest.TestLoader()
    suit = loader.loadTestsFromModule(tests.tests)
    runner = unittest.TextTestRunner()
    runner.run(suit)


if __name__ == "__main__":
    main()
