# AS - IS
class Logistics:
    def deliver(self):
        print('Truck started ...')

l = Logistics()
l.deliver()

# TO - BE

class Truck:
    @staticmethod
    def deliver():
        print('Truck started ...')
class Ship:
    @staticmethod
    def deliver():
        print('Ship started ...')

class Logistics:
    def __init__(self, tt):
        if tt == 'truck':
            self.TransportMode = Truck()
        elif tt == 'ship':
            self.TransportMode = Ship()
        else:
            raise Exception('No such transportMode')
    
    def deliver(self):
        self.TransportMode.deliver()

l = Logistics('ship')
l.deliver()


# improved 

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver():
        pass

class Truck(Transport):
    @staticmethod
    def deliver():
        print('Truck started ...')

class Ship(Transport):
    @staticmethod
    def deliver():
        print('Ship started ...')


def create_transport(transport_mode):
    '''
    define factory function that returns concrete class 
    '''
    if transport_mode == 'ship':
        return Ship()
    elif transport_mode == 'truck':
        return Truck()
    else:
        raise Exception('No such transport')

class Logistics:
    def __init__(self, transport_mode):
        self.transport = create_transport(transport_mode)
    def deliver(self):
        self.transport.deliver()

l = Logistics('ship')
l.deliver()
