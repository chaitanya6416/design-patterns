from abc import ABC, abstractmethod


class Cake(ABC):
    def __init__(self, _name, _kind, _price) -> None:
        self.name = _name
        self.kind = _kind
        self.price = _price
    @abstractmethod
    def recipe():
        pass
    @abstractmethod
    def myFans():
        pass
    def aboutCake(self):
        print(f'this is {self.name} cake')
        self.recipe()
        self.myFans()
        print(f'iam {self.kind} and my price is {self.price}')

class CakeFactory(ABC):
    @abstractmethod
    def create_cake():
        pass

class BlackForest(Cake):
    def __init__(self, _name, _kind, _price) -> None:
        super().__init__(_name, _kind, _price)
    def recipe(self):
        print('...adding x,y,z. making bf')
    def myFans(self):
        print('children are my fans')

class BlackForestFactory(CakeFactory):
    def create_cake(self) -> BlackForest:
        return BlackForest('alpha', 'eggless', 800)

class VanillaCake(Cake):
    def __init__(self, _name, _kind, _price) -> None:
        super().__init__(_name, _kind, _price)
    def recipe(self):
        print('...adding x,y,z. making vanilla cake')
    def myFans(self):
        print('adults are my fans')

class VanillaCakeFactory(CakeFactory):
    def create_cake(self) -> VanillaCake:
        return VanillaCake('beta', 'egg', 900)

class Bakery:
    def __init__(self, _cake_factory):
        self.cake_factory = _cake_factory
    def produce_cake(self):
        cake = self.cake_factory.create_cake()
        return cake

black_forest_bakery = Bakery(BlackForestFactory())
cake1 = black_forest_bakery.produce_cake()
cake1.aboutCake()

vanilla_bakery = Bakery(VanillaCakeFactory())
cake2 = vanilla_bakery.produce_cake()
cake2.aboutCake()
