import pytest
from src.main import Product, Smartphone, LawnGrass, Category, BaseProduct


def test_base_product_abstract():
    """Проверка, что BaseProduct действительно абстрактный"""
    with pytest.raises(TypeError):
        # Создаем и сразу проверяем, что нельзя создать экземпляр
        BaseProduct("Test", "Desc", 100, 1)  # Эта строка вызовет исключение


class TestProduct:
    def test_product_creation(self):
        p = Product("Test", "Desc", 100.0, 5)
        assert p.name == "Test"
        assert p.price == 100.0
        assert p.quantity == 5  # Добавлена проверка quantity

    def test_price_validation(self):
        p = Product("Test", "Desc", 100.0, 5)
        with pytest.raises(ValueError):
            p.price = -50
        assert p.price == 100.0  # Проверяем, что цена не изменилась


class TestSmartphone:
    def test_smartphone_creation(self):
        s = Smartphone("Phone", "Desc", 500.0, 10, 95.5, "Model", 256, "Black")
        assert isinstance(s, Product)
        assert s.memory == 256
        assert s.color == "Black"  # Добавлена проверка цвета


class TestLawnGrass:
    def test_lawn_grass_creation(self):
        lg = LawnGrass("Grass", "Desc", 50.0, 20, "Russia", "7 days", "Green")
        assert isinstance(lg, Product)
        assert lg.country == "Russia"
        assert lg.germination_period == "7 days"  # Добавлена проверка


class TestCategory:
    @pytest.fixture(autouse=True)
    def reset_counters(self):
        Category.reset_counters()
        yield

    def test_category_add_product(self):
        cat = Category("Cat", "Desc")
        p = Product("P", "D", 100.0, 5)
        cat.add_product(p)
        assert cat.product_count == 1
        assert len(cat._products) == 1  # Проверяем добавление продукта

    def test_category_str(self):
        p = Product("P", "D", 100.0, 5)
        cat = Category("Cat", "Desc", [p])
        assert "количество продуктов: 5 шт." in str(cat)
        assert cat.category_count == 1  # Проверяем счетчик категорий


def test_mixin_logging(capsys):
    """Проверка работы миксина логирования"""
    p = Product("Test", "Desc", 100.0, 5)
    captured = capsys.readouterr()
    assert "Создан объект класса Product" in captured.out
    assert p.name == "Test"  # Проверяем, что объект создан корректно


def test_product_addition():
    p1 = Product("P1", "D1", 100.0, 2)
    p2 = Product("P2", "D2", 200.0, 3)
    assert p1 + p2 == 800.0

    s = Smartphone("S", "D", 500.0, 1, 90.0, "M", 256, "Black")
    with pytest.raises(TypeError):
        p1 + s  # type: ignore