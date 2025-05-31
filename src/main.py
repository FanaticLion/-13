from typing import List


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация продукта с валидацией
        :raises ValueError: При недопустимых значениях цены или количества
        """
        if quantity <= 0:
            raise ValueError("Количество товара должно быть положительным")
        if price <= 0:
            raise ValueError("Цена должна быть положительной")

        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = value


class Category:
    _category_count = 0
    _product_count = 0

    def __init__(self, name: str, description: str, initial_products: List[Product] = None):
        """
        Инициализация категории товаров
        :param initial_products: Начальный список товаров (переименован для избежания затенения)
        """
        self.name = name
        self.description = description
        self._products: List[Product] = []

        if initial_products:
            for product in initial_products:
                self.add_product(product)

        Category._category_count += 1

    def middle_price(self) -> float:
        """Вычисляет среднюю цену товаров в категории"""
        if not self._products:
            return 0.0
        return sum(p.price for p in self._products) / len(self._products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Добавлять можно только объекты Product")
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


def demonstrate_usage():
    """Функция для демонстрации работы классов"""
    try:
        # Тест обработки ошибок
        Product("Тест", "Невалидный", -100, 0)
    except ValueError as e:
        print(f"Ожидаемая ошибка: {e}")

    # Создание товаров
    product_list = [
        Product("Galaxy S23", "Флагман Samsung", 180000.0, 5),
        Product("iPhone 15", "Премиум смартфон", 210000.0, 8),
        Product("Redmi Note 11", "Бюджетный", 31000.0, 14)
    ]

    # Работа с категорией
    tech_category = Category("Электроника", "Технические устройства", product_list)
    print(f"Средняя цена: {tech_category.middle_price():.2f} руб.")
    print(f"Всего товаров: {tech_category.product_count}")


if __name__ == '__main__':
    demonstrate_usage()