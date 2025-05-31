# 🛍️ Product and Category Management System

Система управления продуктами и категориями с:
- Подсчётом статистики
- Проверкой типов
- Логированием операций
- Абстрактными классами

## 📦 Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/product-category-system.git
### Структура проекта
cd product-category-system
product-category-system/
├── main.py                 # Основная реализация классов
├── demo.py                 # Примеры использования
├── tests/                  # Тесты
│   ├── test_models.py      # Тесты моделей
│   ├── test_operations.py  # Тесты операций
│   └── conftest.py         # Фикстуры
├── requirements.txt        # Зависимости
└── README.md               # Документация
#### Основные компоненты 
BaseProduct (Абстрактный класс)
class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass 
 Product
class Product(BaseProduct, LoggingMixin):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)
        Smartphone (Наследник Product)
class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color 
Category
class Category:
    _category_count = 0
    _product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.name = name
        self.description = description
        self._products = []
        # ... 
#### Примеры использования 
from main import Product, Smartphone, LawnGrass

# Простой продукт
book = Product("Python Book", "Learn Python", 29.99, 50)

# Смартфон
phone = Smartphone("iPhone 15", "Pro model", 999.99, 10, 
                 95.5, "15 Pro", 256, "Space Gray")

# Газонная трава
grass = LawnGrass("Premium Grass", "Green lawn", 49.99, 100,
                 "USA", "14 days", "Dark Green") 
 Работа с категориями 
 from main import Category

# Создание категории
electronics = Category("Electronics", "Devices and gadgets", [phone])

# Добавление товара
electronics.add_product(Product("Mouse", "Wireless", 19.99, 30))

# Вывод информации
print(electronics)
print(f"Всего товаров: {electronics.product_count}") 
#####✅ Тестирование 
pytest tests/ -v 
Проверка покрытия: 
pytest --cov=main --cov-report=html tests/
open htmlcov/index.html 
📊 Тестовое покрытие

Текущее покрытие тестами составляет 85% (проверено с помощью pytest-cov)

Тесты проверяют:

Создание объектов

Валидацию цен

Операции сложения

Работу категорий

Логирование
 Особенности реализации
Валидация типов

Проверка при сложении продуктов 
def __add__(self, other):
    if type(self) != type(other):
        raise TypeError("Cannot add different product types")
 
Логирование создания объектов 
class LoggingMixin:
    def __init__(self, *args, **kwargs):
        print(f"Created {self.__class__.__name__} instance") 
 Статистика в реальном времени 
class Category:
    _category_count = 0  # Счетчик всех категорий
    _product_count = 0   # Счетчик всех продуктов
#####Возможности для расширения
Добавить поддержку БД (SQLite/PostgreSQL)

Реализовать REST API (FastAPI/Flask)

Добавить систему скидок

Реализовать импорт/экспорт CSV/JSON 
Лицензия
MIT License. Полный текст доступен в файле LICENSE. 