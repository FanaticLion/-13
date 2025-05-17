import pytest
from src.main import Product, Category


class TestProduct:
    """Tests for Product class"""

    def test_product_initialization(self):
        """Test product initialization"""
        product = Product("Test", "Description", 100.0, 5)

        assert product.name == "Test"
        assert product.description == "Description"
        assert product.price == 100.0
        assert product.quantity == 5

    def test_product_attributes_types(self):
        """Test product attribute types"""
        product = Product("Test", "Desc", 99.99, 3)

        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, float)
        assert isinstance(product.quantity, int)


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
        assert len(category.products) == 2
        assert category.products == sample_products

    def test_category_counters(self, sample_products):
        """Test category and product counters"""
        # First category
        category = Category("Category 1", "Desc 1", sample_products)
        assert category.category_count == 1
        assert category.product_count == 2

        # Second category
        Category("Category 2", "Desc 2", [Product("Single", "Desc", 50.0, 1)])
        assert Category._category_count == 2
        assert Category._product_count == 3

    def test_category_properties(self, sample_products):
        """Test category properties"""
        category = Category("Test", "Desc", sample_products)
        assert category.category_count == 1
        assert category.product_count == 2


def test_interaction_between_classes():
    """Test interaction between Product and Category"""
    Category.reset_counters()

    products = [
        Product("P1", "D1", 10.0, 2),
        Product("P2", "D2", 20.0, 3)
    ]

    category = Category("Category", "Description", products)

    assert len(category.products) == 2
    assert category.products[0].name == "P1"
    assert category.products[1].price == 20.0
    assert category.category_count == 1
    assert category.product_count == 2

78