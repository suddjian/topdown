class Test:
    def __init__(self):
        self.var = 5

    def test(self):
        return self.var

    def calltest(self):
        print str(self.test())
