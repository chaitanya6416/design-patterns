from abc import ABC, abstractmethod

class DeliveryService(ABC):
    @abstractmethod
    def calculate_cost(self, origin, destination, package_weight):
        pass

    @abstractmethod
    def track_package(self, tracking_number):
        pass

    @abstractmethod
    def deliver_package(self, package_details):
        pass



