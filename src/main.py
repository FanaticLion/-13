class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Initialize a Product instance.
        Args:
            name: Name of the product
            description: Description of the product
            price: Price of the product
            quantity: Quantity available in stock
        """
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут
        self.quantity = quantity

    def __str__(self) -> str:
        """Возвращает строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """
        Сложение двух продуктов.
        Возвращает сумму произведений цены на количество для каждого продукта.
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с валидацией"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = new_price


class Category:
    _category_count: int = 0  # Private class attribute with type hint
    _product_count: int = 0  # Private class attribute with type hint

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Initialize a Category instance.
        Args:
            name: Name of the category
            description: Description of the category
            products: List of Product objects in this category
        """
        self.name = name
        self.description = description
        self._products = products  # Приватный атрибут

        # Increment counters
        Category._category_count += 1
        Category._product_count += len(products)

    def __str__(self) -> str:
        """Возвращает строковое представление категории"""
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию"""
        self._products.append(product)
        Category._product_count += 1

    @property
    def products(self) -> str:
        """Геттер для форматированного вывода продуктов"""
        return "\n".join(str(product) for product in self._products)

    @classmethod
    def new_product(cls, product_data: dict) -> Product:
        """Создает новый продукт из словаря"""
        return Product(
            name=product_data.get('name'),
            description=product_data.get('description'),
            price=product_data.get('price'),
            quantity=product_data.get('quantity')
        )

    @classmethod
    def reset_counters(cls) -> None:
        """Reset all counters (for testing purposes)"""
        cls._category_count = 0
        cls._product_count = 0

    @property
    def category_count(self) -> int:
        """Get total number of categories"""
        return Category._category_count

    @property
    def product_count(self) -> int:
        """Get total number of products across all categories"""
        return Category._product_count


if __name__ == "__main__":
    # Example usage
    Category.reset_counters()

    p1 = Product("Phone", "Smartphone", 500.0, 10)
    p2 = Product("Laptop", "Gaming laptop", 1500.0, 5)

    # Тестирование __str__ для Product
    print("Тест __str__ для Product:")
    print(p1)  # Выведет: Phone, 500.0 руб. Остаток: 10 шт.
    print(p2)  # Выведет: Laptop, 1500.0 руб. Остаток: 5 шт.

    # Тестирование __add__ для Product
    print("\nТест __add__ для Product:")
    total_value = p1 + p2
    print(f"Общая стоимость товаров: {total_value} руб.")  # Выведет: 5000 + 7500 = 12500 руб.

    electronics = Category("Electronics", "Electronic devices", [p1, p2])

    # Тестирование __str__ для Category
    print("\nТест __str__ для Category:")
    print(electronics)  # Выведет: Electronics, количество продуктов: 15 шт.

    # Добавляем новый продукт
    p3 = Product("Tablet", "Android tablet", 300.0, 8)
    electronics.add_product(p3)

    # Проверяем обновленное количество
    print("\nПосле добавления Tablet:")
    print(electronics)  # Выведет: Electronics, количество продуктов: 23 шт.

    # Создаем продукт через класс-метод
    p4_data = {"name": "Mouse", "description": "Wireless mouse", "price": 50.0, "quantity": 20}
    p4 = Category.new_product(p4_data)
    electronics.add_product(p4)

    print("\nПосле добавления Mouse:")
    print(electronics)  # Выведет: Electronics, количество продуктов: 43 шт.

    print("\nСписок продуктов:")
    print(electronics.products)

    # Тестируем сеттер цены
    p1.price = -100  # Должно вывести сообщение об ошибке
    p1.price = 600   # Корректное обновление цены
    print(f"\nNew price for {p1.name}: {p1.price}")