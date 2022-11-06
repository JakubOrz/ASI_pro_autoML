def drawTree(height: int = 5):
    for i in range(height):
        print("{0}{1}".format(" "*(height-i), "*"*i))


def drawBetterTree(height: int = 5):
    for i in range(height):
        print("{0}{1}".format(" " * (height - i), "*" * (i + (i - 1))))


