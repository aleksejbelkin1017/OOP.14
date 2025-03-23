import pytest

from src.category import Category
from src.product import Product


# Тесты для класса Category
def test_category_init(category):
    """Тест инициализации объекта Category"""
    assert category.name == "Смартфоны"
    assert category.description == "Категории современных смартфонов"
    assert len(category.products) == 3


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


def test_product_quantity_count(category):
    """Тест подсчета общего количества товаров на складе"""
    assert sum(p.quantity for p in category.products) == 27
