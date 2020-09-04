import abc


class Beverage(metaclass=abc.ABCMeta):
    description = "Unknown Beverage"

    def getDescription(self):
        return self.description

    @abc.abstractmethod
    def cost(self) -> float:
        pass


class CondimentDecorator(Beverage):
    @abc.abstractmethod
    def getDescription(self):
        pass


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99


class DarkRoast(Beverage):
    def __init__(self):
        self.description = "DarkRoast"

    def cost(self) -> float:
        return 0.49


class HouseBlend(Beverage):
    def __init__(self):
        self.description = "HouseBlend"

    def cost(self) -> float:
        return 0.89


class Mocha(CondimentDecorator):
    beverage: Beverage

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription()+ ", Mocha"

    def cost(self) -> float:
        return round(self.beverage.cost() + 0.20, 2)


class Soy(CondimentDecorator):
    beverage: Beverage

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription()+ ", Soy"

    def cost(self) -> float:
        return round(self.beverage.cost() + 0.30, 2)


class Whip(CondimentDecorator):
    beverage: Beverage

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription()+ ", Whip"

    def cost(self) -> float:
        return round(self.beverage.cost() + 0.10, 2)