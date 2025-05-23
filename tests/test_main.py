import pytest
from src.main import Product, Category


class TestProduct:
    """Tests for Product class"""

    def test_product_str(self):
        """Test __str__ method for Product"""
        product = Product("Test", "Description", 100.0, 5)
        expected = "Test, 100.0 руб. Остаток: 5 шт."
        assert str(product) == expected

    def test_product_add(self):
        """Test __add__ method for Product"""
        p1 = Product("P1", "D1", 100.0, 2)
        p2 = Product("P2", "D2", 200.0, 3)

        # Test valid addition
        assert p1 + p2 == 100.0 * 2 + 200.0 * 3

        # Test invalid addition
        with pytest.raises(TypeError):
            p1 + "not a product"


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

    def test_category_str(self, sample_products):
        """Test __str__ method for Category"""
        category = Category("Test", "Description", sample_products)
        expected = "Test, количество продуктов: 8 шт."
        assert str(category) == expected

        # Test after adding product
        category.add_product(Product("New", "New desc", 50.0, 2))
        expected = "Test, количество продуктов: 10 шт."
        assert str(category) == expected