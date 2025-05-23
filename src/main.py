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

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию"""
        self._products.append(product)
        Category._product_count += 1

    @property
    def products(self) -> str:
        """Геттер для форматированного вывода продуктов"""
        products_str = ""
        for product in self._products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

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

    electronics = Category("Electronics", "Electronic devices", [p1, p2])

    # Добавляем новый продукт
    p3 = Product("Tablet", "Android tablet", 300.0, 8)
    electronics.add_product(p3)

    # Создаем продукт через класс-метод
    p4_data = {"name": "Mouse", "description": "Wireless mouse", "price": 50.0, "quantity": 20}
    p4 = Category.new_product(p4_data)
    electronics.add_product(p4)

    print(f"Total categories: {electronics.category_count}")
    print(f"Total products: {electronics.product_count}")
    print("Products in this category:")
    print(electronics.products)

    # Тестируем сеттер цены
    p1.price = -100  # Должно вывести сообщение об ошибке
    p1.price = 600   # Корректное обновление цены
    print(f"New price for {p1.name}: {p1.price}")