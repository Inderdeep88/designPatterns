from decorator.Beverages import Espresso, DarkRoast, Mocha, Whip, HouseBlend, Soy

if __name__ == "__main__":
    beverage = Espresso()
    print(beverage.getDescription()+" $",beverage.cost())

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.getDescription()+" $",beverage2.cost())

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.getDescription()+" $",beverage3.cost())