class Stock():
    def __init__(self, product, count = 0, id = None):
        self.product = product
        self.count = count
        self.id = id

    def modify_count(self,value):
        self.count = self.count + value

