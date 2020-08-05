string = 0


#  TEST #

def assertEquals(firstComparing, secondComparing):
    if firstComparing == secondComparing:
        return True
    else:
        return False


def testStringToInt(string):
    print(assertEquals(string, 4))
