

#  TEST #

def assertEquals(firstComparing, secondComparing):
    if firstComparing == secondComparing:
        return True
    else:
        return False


def testStringToInt():
    print(assertEquals(string.convert('Deux'),2))
    print(assertEquals(string.convert('Trois'),3))
    print(assertEquals(string.convert('Plus'),"+"))
    print(assertEquals(string.convert('Moins'),"-"))
    print(assertEquals(string.convert('DeuxPlusDeux'),4))
    print(assertEquals(string.convert('TroisMoinsDeux'),1))
    print(assertEquals(string.convert('TroisMoinsDeuxPlusCinqMoinsSix'),0))
