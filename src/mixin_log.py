# from src.product import Product, Smartphone, LawnGrass


class MyLogMixin:

    def __init__(self):
        log_str = f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity}"
        prod_str = ")"

        if self.__class__.__name__ == "Product":
            log_str += prod_str

        if self.__class__.__name__ == "Smartphone":
            smart_str = f", '{self.efficiency}', '{self.model}', '{self.memory}', '{self.color}'"
            log_str = log_str + smart_str + prod_str

        if self.__class__.__name__ == "LawnGrass":
            log_str += (
                f", '{self.country}', '{self.germination_period}', '{self.color}'"
                + prod_str
            )

        print(log_str)
        super().__init__()
