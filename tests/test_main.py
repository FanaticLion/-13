import pytest
from src.main import Product, Smartphone, LawnGrass, Category


class TestProduct:
    def test_product_creation(self):
        p = Product("Test", "Desc", 100.0, 5)
        assert p.name == "Test"
        assert p.description == "Desc"
        assert p.price == 100.0
        assert p.quantity == 5

    def test_price_validation(self):
        p = Product("Test", "Desc", 100.0, 5)
        with pytest.raises(ValueError):
            p.price = -50
        p.price = 150.0
        assert p.price == 150.0

    def test_product_str(self):
        p = Product("Test", "Desc", 100.0, 5)
        assert str(p) == "Test, 100.0 руб. Остаток: 5 шт."

    def test_product_add(self):
        p1 = Product("P1", "D1", 100.0, 2)
        p2 = Product("P2", "D2", 200.0, 3)
        assert p1 + p2 == 800.0

        with pytest.raises(TypeError):
            p1 + "invalid"  # type: ignore


class TestSmartphone:
    def test_smartphone_creation(self):
        s = Smartphone("Phone", "Desc", 500.0, 10, 95.5, "Model", 256, "Black")
        assert s.name == "Phone"
        assert s.efficiency == 95.5
        assert s.model == "Model"
        assert s.memory == 256
        assert s.color == "Black"


class TestLawnGrass:
    def test_lawn_grass_creation(self):
        lg = LawnGrass("Grass", "Desc", 50.0, 20, "Russia", "7 days", "Green")
        assert lg.name == "Grass"
        assert lg.country == "Russia"
        assert lg.germination_period == "7 days"
        assert lg.color == "Green"


class TestCategory:
    @pytest.fixture(autouse=True)
    def reset_counters(self):
        Category.reset_counters()
        yield

    def test_category_creation(self):
        p = Product("P", "D", 100.0, 5)
        cat = Category("Cat", "Desc", [p])
        assert cat.name == "Cat"
        assert str(cat) == "Cat, количество продуктов: 5 шт."

    def test_add_product(self):
        cat = Category("Cat", "Desc")
        p = Product("P", "D", 100.0, 5)
        cat.add_product(p)
        assert len(cat._products) == 1
        assert "P, 100.0 руб. Остаток: 5 шт." in cat.products

        with pytest.raises(TypeError):
            cat.add_product("invalid")  # type: ignore

    def test_counters(self):
        Category.reset_counters()
        p1 = Product("P1", "D1", 100.0, 5)
        p2 = Product("P2", "D2", 200.0, 3)

        # Создаем и используем обе категории
        cat1 = Category("Cat1", "Desc1", [p1])
        cat2 = Category("Cat2", "Desc2", [p2])

        assert cat1.category_count == 2
        assert cat2.product_count == 2
        assert cat2.category_count == 2  # Используем cat2


def test_product_addition_compatibility():
    p1 = Product("P1", "D1", 100.0, 2)
    p2 = Product("P2", "D2", 200.0, 3)
    s = Smartphone("S", "SD", 500.0, 1, 90.0, "M", 256, "Black")

    assert p1 + p2 == 800.0

    with pytest.raises(TypeError):
        p1 + s  # type: ignore