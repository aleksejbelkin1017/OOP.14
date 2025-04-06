import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


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
def category():
    product1 = Product("iPhone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("iPhone 14", "256GB, Silver", 180000.0, 5)
    product3 = Product("iPhone 13", "128GB, Black", 150000.0, 3)
    return Category("Смартфоны", "Категории смартфонов", [product1, product2, product3])


# Фикстура для тестов homework 14.2
@pytest.fixture
def product():
    return Product("iPhone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category2():
    product1 = Product("iPhone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("iPhone 14", "256GB, Silver", 180000.0, 5)
    return Category("Смартфоны", "Категории смартфонов", [product1, product2])


# Фикстуры для создания объектов для тестов homework 16.1
@pytest.fixture
def smartphone1():
    return Smartphone("Samsung Galaxy S23 Ultra",
                      "256GB, Серый цвет, 200MP камера",
                      180000.0,
                      5,
                      95.5,
                      "S23 Ultra",
                      256,
                      "Серый")


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15",
                      "512GB, Gray space",
                      210000.0, 8, 98.2,
                      "15", 512, "Gray space")


@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава",
                     "Элитная трава для газона",
                     500.0, 20, "Россия",
                     "7 дней", "Зеленый")


@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2",
                     "Выносливая трава",
                     450.0, 15, "США",
                     "5 дней", "Темно-зеленый")
