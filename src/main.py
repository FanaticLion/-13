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
        self.price = price
        self.quantity = quantity


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
        self.products = products

        # Increment counters
        Category._category_count += 1
        Category._product_count += len(products)

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

    print(f"Total categories: {electronics.category_count}")
    print(f"Total products: {electronics.product_count}")
    print(f"Products in this category: {len(electronics.products)}")

