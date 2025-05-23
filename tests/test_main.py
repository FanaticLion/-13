import pytest
from src.main import Product, Category


class TestProduct:
    """Tests for Product class"""

    def test_product_initialization(self):
        """Test product initialization"""
        product = Product("Test", "Description", 100.0, 5)

        assert product.name == "Test"
        assert product.description == "Description"
        assert product.price == 100.0  # Используем property-геттер
        assert product.quantity == 5

    def test_product_price_validation(self):
        """Test price validation in setter"""
        product = Product("Test", "Desc", 100.0, 1)

        # Попытка установить отрицательную цену
        product.price = -50
        assert product.price == 100.0  # Цена не изменилась

        # Корректное изменение цены
        product.price = 150.0
        assert product.price == 150.0


class TestCategory:
    """Tests for Category class"""

    @pytest.fixture(autouse=True)
    def reset_counters(self):
        """Auto-reset counters before each test"""
        Category.reset_counters()
        yield

    @pytest.fixture
    def sample_products(self) -> list[Product]:
        """Sample products fixture"""
        return [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 3)
        ]

    def test_category_initialization(self, sample_products):
        """Test category initialization"""
        category = Category("Test", "Description", sample_products)

        assert category.name == "Test"
        assert category.description == "Description"
        # Проверяем форматированную строку продуктов
        assert "Product 1, 100.0 руб. Остаток: 5 шт." in category.products
        assert "Product 2, 200.0 руб. Остаток: 3 шт." in category.products

    def test_add_product(self, sample_products):
        """Test adding product to category"""
        category = Category("Test", "Desc", sample_products)
        initial_count = category.product_count

        new_product = Product("New", "New desc", 50.0, 10)
        category.add_product(new_product)

        assert "New, 50.0 руб. Остаток: 10 шт." in category.products
        assert category.product_count == initial_count + 1

    def test_new_product_classmethod(self):
        """Test new_product class method"""
        product_data = {
            "name": "Test Product",
            "description": "Test Desc",
            "price": 99.99,
            "quantity": 7
        }
        product = Category.new_product(product_data)

        assert isinstance(product, Product)
        assert product.name == "Test Product"
        assert product.price == 99.99


def test_interaction_between_classes():
    """Test interaction between Product and Category"""
    Category.reset_counters()

    # Создаем продукты через класс-метод
    p1 = Category.new_product({"name": "P1", "description": "D1", "price": 10.0, "quantity": 2})
    p2 = Category.new_product({"name": "P2", "description": "D2", "price": 20.0, "quantity": 3})

    category = Category("Category", "Description", [p1, p2])

    # Проверяем через property-геттер
    assert "P1, 10.0 руб. Остаток: 2 шт." in category.products
    assert "P2, 20.0 руб. Остаток: 3 шт." in category.products
    assert category.category_count == 1
    assert category.product_count == 2