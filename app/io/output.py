def printConsole(text):
    """
    Prints text to the console
    :param text: what to write to the console
    :return: void
    """
    print(text)

def writeFile(filename, text):
    """
    Writes to the file
    :param filename: name of the file to write to
    :param text: what to write to the file
    :return: void
    """
    try:
        with open(filename, 'w') as file:
            text = file.write(text)
    except FileNotFoundError:
        raise FileNotFoundError
    except FileExistsError:
        raise FileExistsError