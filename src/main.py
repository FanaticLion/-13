from typing import List


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация продукта с валидацией
        :raises ValueError: При недопустимых значениях цены или количества
        """
        if quantity == 0:  # Строго проверяем на ноль
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        if quantity < 0 or price <= 0:
            raise ValueError("Количество должно быть положительным и цена должна быть положительной")

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
        self.name = name
        self.description = description
        self._products: List[Product] = []

        if initial_products:
            for product in initial_products:
                self.add_product(product)

        Category._category_count += 1

    def middle_price(self) -> float:
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
    """Демонстрация работы с обработкой ошибок"""
    try:
        # Проверка точного сообщения для нулевого количества
        Product("Тест", "Нулевое количество", 100, 0)
    except ValueError as e:
        assert str(e) == "Товар с нулевым количеством не может быть добавлен", "Неверное сообщение об ошибке"
        print("Тест сообщения об ошибке пройден")

    # Создание и работа с корректными данными
    try:
        products = [
            Product("Galaxy S23", "Флагман", 180000.0, 5),
            Product("iPhone 15", "Премиум", 210000.0, 8)
        ]
        tech = Category("Смартфоны", "Мобильные устройства", products)
        print(f"Средняя цена: {tech.middle_price():.2f} руб.")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == '__main__':
    demonstrate_usage()