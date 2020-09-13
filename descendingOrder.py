class descendingOrder:
    def __init__(self):
        pass

    def descending(self,test):
        print(self.convertStringToInteger(self.split(test)))
        return self.convertStringToInteger(self.split(test))

    def split(self, test):
        return [char for char in test]

    def convertStringToInteger(self,test_list):
        return list(map(int, test_list))