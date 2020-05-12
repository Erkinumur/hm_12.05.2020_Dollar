class MoneyFmt:
    def __init__(self, value):
        self.value = value
        if value < 0:
            self._char = '-'
        else:
            self._char = ''
            
    def _dollarize(self):   
        if self.value == int(self.value):
            return f'{self._char}${abs(self.value):,}'
        else:
            return f'{self._char}${abs(self.value):,.2f}'
        
    def __str__(self):
        return self._dollarize()
    
    def __repr__(self):
        return str(self.value)

    def update(self, value):
        self.__init__(value)


cash = MoneyFmt(12345678.021)
print(cash)
cash.update(100000.4567)
print(cash)
cash.update(-0.3)
print(cash)
print(repr(cash))
