def readfile(direction):
    f = open(direction, "r")
    data = f.readlines()
    f.close()
    return data

def writefile(direction, userinput):
    