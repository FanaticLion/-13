from abc import ABC, abstractmethod
from typing import List, Union


class LoggingMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        print(f"Создан объект класса {self.__class__.__name__} с параметрами:")
        print(f"Атрибуты: {args}")
        print(f"Ключевые атрибуты: {kwargs}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        pass


class Product(BaseProduct, LoggingMixin):
    """Основной класс продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name=name, description=description, price=price, quantity=quantity)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных категорий")
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = value


class Smartphone(Product):
    """Класс для смартфонов"""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для газонной травы"""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Класс для категорий товаров"""
    _category_count = 0
    _product_count = 0

    def __init__(self, name: str, description: str, products: List[Product] = None):
        self.name = name
        self.description = description
        self._products: List[Product] = []

        if products:
            for product in products:
                self.add_product(product)

        Category._category_count += 1

    def __str__(self) -> str:
        total_quantity = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")
        self._products.append(product)
        Category._product_count += 1

    @property
    def products(self) -> str:
        return "\n".join(str(p) for p in self._products)

    @classmethod
    def reset_counters(cls) -> None:
        cls._category_count = 0
        cls._product_count = 0

    @property
    def category_count(self) -> int:
        return Category._category_count

    @property
    def product_count(self) -> int:
        return Category._product_count


if __name__ == '__main__':
    # Демонстрация работы
    smartphone = Smartphone("Samsung Galaxy", "Flagship smartphone", 100000, 10,
                            95.5, "S23", 256, "Black")
    lawn_grass = LawnGrass("Premium Grass", "High quality grass", 5000, 100,
                           "USA", "2 weeks", "Green")

    category = Category("Electronics", "Electronic devices", [smartphone])
    category.add_product(lawn_grass)

    print(category)
    print(category.products)