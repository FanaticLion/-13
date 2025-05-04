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
    # Class attributes for counting
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
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

        # Increment category counter
        Category.category_count += 1

        # Increment product counter by the number of products in this category
        Category.product_count += len(products)

    @property
    def category_count(self):
        """Getter for the class attribute category_count"""
        return Category.category_count

    @property
    def product_count(self):
        """Getter for the class attribute product_count"""
        return Category.product_count