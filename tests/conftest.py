import pytest

from src.category import Category
from src.product import Product


# Фикстуры для продуктов
@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0,
                   5)


@pytest.fixture
def product2():
    return Product("Iphone 15",
                   "512GB, Gray space",
                   210000.0,
                   8)


@pytest.fixture
def product3():
    return Product("Xiaomi Redmi Note 11",
                   "1024GB, Синий",
                   31000.0,
                   14)


# Фикстура для категории с продуктами
@pytest.fixture
def category(product1, product2, product3):
    category = Category("Смартфоны",
                        "Категории современных смартфонов",
                        [product1, product2, product3])
    return category
