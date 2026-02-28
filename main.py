from app.io.input import readConsole, readFile, readFilePandas
from app.io.output import writeFile, printConsole

def main():
    text = readConsole()
    printConsole(text)
    text3 = readFile("testFiles/test1.txt")
    writeFile("testFiles/test1Res.txt", str(text3))
    text2 = readFilePandas("testFiles/test1.txt")
    writeFile("testFiles/test1ResP.txt", str(text2))

if __name__ == "__main__":
    main()
