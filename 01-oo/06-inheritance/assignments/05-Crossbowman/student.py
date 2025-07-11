class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if self.__num_arrows >= num:
            self.__num_arrows -= num
        else:
            raise ValueError("Not enough arrows")


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        if self.get_num_arrows() < 3:
            raise ValueError("Not enough arrows")
        else:
            self.use_arrows(3)
        return f"{target} was shot by 3 crossbow bolts"