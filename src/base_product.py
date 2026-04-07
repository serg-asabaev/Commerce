from abc import ABC, abstractmethod

class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass


    @abstractmethod
    def new_product(self, params:dict):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass