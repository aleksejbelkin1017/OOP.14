import pytest

from src.category import Category
from src.product import Product


# Тесты для класса Category
def test_category_init(category):
    """Тест инициализации объекта Category"""
    assert category.name == "Смартфоны"
    assert category.description == "Категории смартфонов"
    assert len(category._products) == 3


def test_category_empty_products():
    """Тест создания категории без продуктов"""
    category = Category("Empty Category",
                        "No products",
                        [])
    assert len(category.products) == 0


def test_category_invalid_products():
    """Тест на неверный тип продуктов"""
    with pytest.raises(TypeError):
        Category("Invalid",
                 "Desc",
                 "not a list")


# Тесты для счетчиков
def test_category_count():
    """Тест подсчета количества категорий"""
    Category.category_count = 0  # Сброс счетчика
    # Создаем первую категорию через переданную фикстуру
    Category("Смартфоны", "Категории современных смартфонов", [])
    # Проверяем, что счетчик обновился после создания первой категории
    assert Category.category_count == 1
    # Создаем вторую категорию напрямую
    Category("Cat 2", "Desc 2", [])
    # Проверяем, что счетчик обновился после создания второй категории
    assert Category.category_count == 2


def test_product_count(category):
    """Тест подсчета количества продуктов"""
    Category.product_count = 0
    # Создаем категорию с одним продуктом
    Category("Cat", "Desc", [Product("P1", "Desc", 100, 5)])
    # Проверяем, что счетчик учитывает все продукты
    assert Category.product_count == 1
    # Создаем категорию с несколькими продуктами
    Category("Cat 2", "Desc 2", [
        Product("P2", "Desc", 200, 5),
        Product("P3", "Desc", 300, 5)
    ])
    assert Category.product_count == 3


def test_product_quantity_count(category2):
    # Если products возвращает строку, парсим её
    product_lines = category2.products.split('\n')
    quantity_sum = sum(int(line.split('Остаток: ')[1].replace(' шт.', '')) for line in product_lines)
    assert quantity_sum == 13  # 8 + 5


def test_private_products_attribute(category2):
    # Проверка, что _products является приватным
    assert category2._products is not None  # Проверяем, что атрибут существует


def test_products_property(category2):
    # Проверка работы property products
    expected_output = (
        "iPhone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "iPhone 14, 180000.0 руб. Остаток: 5 шт."
    )
    assert category2.products == expected_output


def test_add_product_property(category2):
    # Проверка добавления продукта и обновления property
    new_product = Product("iPhone 13", "128GB, Black", 150000.0, 3)
    category2.add_product(new_product)

    expected_output = (
        "iPhone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "iPhone 14, 180000.0 руб. Остаток: 5 шт.\n"
        "iPhone 13, 150000.0 руб. Остаток: 3 шт."
    )
    assert category2.products == expected_output


def test_invalid_product_addition(category2):
    # Проверка обработки ошибки при добавлении некорректного продукта
    with pytest.raises(TypeError):
        category2.add_product("Некорректный продукт")