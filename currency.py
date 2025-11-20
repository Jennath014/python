class Currency:
    def __init__(self,amount,unit):
        self.amount=amount
        self.unit=unit

    def __eq__(self,other):
        return  self.amount == other.amount and self.unit == other.unit

c1 = Currency(4000,'INR')
c2 = Currency(3000,'INR')
c3 = Currency(4000,'INR')
print(c1==c2)
print(c1.__eq__(c3))
