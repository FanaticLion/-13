from typing import List, Union


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Базовый класс для товаров
        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество товара в наличии
        """
        self.name = name
        self.description = description
        self._price = price  # Защищенный атрибут цены
        self.quantity = quantity

    def __str__(self) -> str:
        """Строковое представление товара"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:
        """
        Сложение товаров по стоимости с учетом количества
        :param other: Другой товар того же класса
        :return: Общая стоимость
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных категорий")
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с валидацией"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        """
        Класс для смартфонов (наследник Product)
        :param efficiency: Производительность
        :param model: Модель
        :param memory: Объем памяти (ГБ)
        :param color: Цвет
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        """
        Класс для газонной травы (наследник Product)
        :param country: Страна-производитель
        :param germination_period: Срок прорастания
        :param color: Цвет
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    _category_count: int = 0
    _product_count: int = 0

    def __init__(self, name: str, description: str,
                 products: List[Union[Product, Smartphone, LawnGrass]] = None):
        """
        Класс для категорий товаров
        :param name: Название категории
        :param description: Описание категории
        :param products: Список товаров в категории
        """
        self.name = name
        self.description = description
        self._products: List[Union[Product, Smartphone, LawnGrass]] = []

        if products:
            for product in products:
                self.add_product(product)

        Category._category_count += 1

    def __str__(self) -> str:
        """Строковое представление категории"""
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Union[Product, Smartphone, LawnGrass]) -> None:
        """
        Добавление товара в категорию
        :param product: Товар (должен быть экземпляром Product или его наследников)
        """
        if not isinstance(product, (Product, Smartphone, LawnGrass)):
            raise TypeError("Можно добавлять только объекты Product или его подклассы")

        self._products.append(product)
        Category._product_count += 1

    @property
    def products(self) -> str:
        """Получение форматированного списка товаров"""
        return "\n".join(str(product) for product in self._products)

    @classmethod
    def new_product(cls, product_data: dict) -> Product:
        """Создание нового товара из словаря"""
        return Product(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    @classmethod
    def reset_counters(cls) -> None:
        """Сброс счетчиков категорий и товаров"""
        cls._category_count = 0
        cls._product_count = 0

    @property
    def category_count(self) -> int:
        """Получение количества категорий"""
        return Category._category_count

    @property
    def product_count(self) -> int:
        """Получение количества товаров"""
        return Category._product_count