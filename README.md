# Product and Category Management System

Проект предоставляет классы для управления продуктами и категориями с подсчётом статистики.

## 🛠 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-репозиторий.git
   cd ваш-репозиторий 
   pip install pytest  # для запуска тестов
### tests/
├── test_initialization.py  # Тесты инициализации
├── test_counters.py        # Тесты счётчиков
└── test_integration.py     # Интеграционные тесты
####  Пример использования
from models import Product, Category

# Создание товаров
p1 = Product("Laptop", "Gaming", 1500.0, 5)
p2 = Product("Mouse", "Wireless", 50.0, 20)

# Создание категории
electronics = Category("Electronics", "Devices", [p1, p2])

print(f"Всего категорий: {electronics.category_count}")
print(f"Всего товаров: {electronics.product_count}")
##### Статистика
Category("Books", "", [Product(...)])  # Увеличит счётчики


Этот README:
- Полностью соответствует вашему коду
- Содержит примеры использования
- Описывает систему тестирования
- Имеет чёткую структуру
- Поддерживает Markdown-форматирование

Для использования:
1. Сохраните как `README.md` в корне проекта
2. Добавьте в Git:
   ```bash
   git add README.md
   git commit -m "Add project documentation"
   git push origin main