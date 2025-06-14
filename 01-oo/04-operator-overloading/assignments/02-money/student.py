class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
       
    def amount(self):
        return self.amount
    
    def currency(self):
        return self.currency
    
    def __add__(self, other):
        if isinstance(Money, int or float) and self.currency == other.currency:
            return self.amount + other.amount
        else:
            raise RuntimeError("Mismatched currencies!")
        
    def __sub__(self, other):
        if isinstance(Money, int or float) and self.currency == other.currency:
            return self.amount - other.amount
        else:
            raise RuntimeError("Mismatched currencies!")
    
    def __mul__(self, number):
        if isinstance(Money, int or float):
            return self.amount * number
        
    
        


money = Money(10, "EUR")


money.amount
money.currency

Money(10, "EUR") + Money(20, "EUR")
Money(10, "EUR") + Money(20, "USD")

Money(30, "EUR") - Money(10, "EUR")
Money(30, "EUR") - Money(10, "USD")

Money(20, "EUR") * 5