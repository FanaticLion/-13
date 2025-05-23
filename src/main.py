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

    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        return self._price * self.quantity + other._price * other.quantity

    @property
    def price(self):
        """Геттер для цены"""
        return self._price

    @price.setter
    def price(self, value):
        """Сеттер для цены с валидацией"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value


class Category:
    _category_count = 0
    _product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.name = name
        self.description = description
        self._products = []

        if products:
            for product in products:
                self.add_product(product)

        Category._category_count += 1

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        """Добавляет продукт в категорию с проверкой типа"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product или его подклассы")

        self._products.append(product)
        Category._product_count += 1

    @property
    def products(self):
        """Геттер для форматированного вывода продуктов"""
        return "\n".join(str(product) for product in self._products)

    @classmethod
    def new_product(cls, product_data: dict):
        """Создает новый продукт из словаря"""
        return Product(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    @classmethod
    def reset_counters(cls):
        """Сбрасывает счетчики"""
        cls._category_count = 0
        cls._product_count = 0

    @property
    def category_count(self):
        return self._category_count

    @property
    def product_count(self):
        return self._product_count


if __name__ == "__main__":
    # Тестирование
    Category.reset_counters()

    try:
        p1 = Product("Phone", "Smartphone", 500.0, 10)
        p2 = Product("Laptop", "Gaming laptop", 1500.0, 5)

        # Проверка сложения продуктов
        print(f"Общая стоимость: {p1 + p2} руб.")

        # Проверка добавления неправильного типа
        electronics = Category("Electronics", "Electronic devices")
        electronics.add_product(p1)

        try:
            electronics.add_product("Not a product")
        except TypeError as e:
            print(f"Ошибка: {e}")

        # Проверка сеттера цены
        p1.price = -100  # Должно вывести сообщение об ошибке
        p1.price = 600  # Корректное обновление

        print(p1)
        print(electronics)

    except Exception as e:
        print(f"Произошла ошибка: {e}")