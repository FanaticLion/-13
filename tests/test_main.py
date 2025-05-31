import pytest
from src.main import Product, Category


class TestProduct:
    def test_zero_quantity_validation(self):
        """Тест обработки нулевого количества"""
        with pytest.raises(ValueError) as excinfo:
            Product("Test", "Desc", 100.0, 0)
        assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)

    def test_valid_product_creation(self):
        """Тест создания валидного продукта"""
        p = Product("Test", "Desc", 100.0, 1)
        assert p.quantity == 1


class TestCategory:
    @pytest.fixture(autouse=True)
    def reset_counters(self):
        Category.reset_counters()
        yield

    @pytest.fixture
    def sample_products(self):
        return [
            Product("P1", "D1", 100.0, 1),
            Product("P2", "D2", 200.0, 2),
            Product("P3", "D3", 300.0, 3)
        ]

    def test_middle_price_calculation(self, sample_products):
        """Тест расчета средней цены"""
        category = Category("Test", "Desc", sample_products)
        assert category.middle_price() == 200.0  # (100+200+300)/3 = 200

    def test_empty_category_middle_price(self):
        """Тест средней цены для пустой категории"""
        category = Category("Empty", "Desc")
        assert category.middle_price() == 0

    def test_add_product_increases_count(self):
        """Тест увеличения счетчика при добавлении"""
        category = Category("Test", "Desc")
        initial_count = category.product_count
        category.add_product(Product("P", "D", 100.0, 1))
        assert category.product_count == initial_count + 1


def test_main_scenario():
    """Интеграционный тест основного сценария"""
    try:
        Product("Invalid", "Desc", 100.0, 0)
        assert False, "Должна была возникнуть ошибка"
    except ValueError:
        pass

    valid_products = [
        Product("P1", "D1", 100.0, 1),
        Product("P2", "D2", 200.0, 2)
    ]
    category = Category("Test", "Desc", valid_products)
    assert category.middle_price() == 150.0