import pandas

def readConsole():
    """
    Reads contents from the console
    :return: string with contents, returns empty string if there was nothing there
    """
    return input()

def readFile(filename):
    """
    Reads contents of the file using python native tools
    :param filename: The name of the file to read
    :return:
        returns contents of the file, or nothing if the file is empty
        throws an error if the file is not found
    """
    try:
        with open(filename, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        raise FileNotFoundError
    except FileExistsError:
        raise  FileExistsError

def readFilePandas(filename):
    """
    Reads contents of the file using pandas library
    :param filename: The name of the file to read
    :return: returns contents of the file, or nothing if the file is empty
    """
    text = pandas.read_csv(filename)
    return text