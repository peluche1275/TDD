class descendingOrder:
    def __init__(self):
        pass

    def descending(self,test):
        testtdd = self.convertStringToInteger(self.split(test))
        testtdd.sort(reverse=True)
        strings = [str(integer) for integer in testtdd]
        a_string = "".join(strings)
        an_integer = int(a_string)
        return an_integer

    def split(self, test):
        return [char for char in test]

    def convertStringToInteger(self,test_list):
        return list(map(int, test_list))