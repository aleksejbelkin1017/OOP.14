import pytest

from src.product import Product


# Тесты для класса Product
def test_product_init(product1):
    """Тест инициализации объекта Product"""
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_product_invalid_price():
    """Тест на неверный тип цены"""
    with pytest.raises(TypeError):
        Product("Test", "Desc", "invalid", 5)


def test_product_invalid_quantity():
    """Тест на неверный тип количества"""
    with pytest.raises(TypeError):
        Product("Test", "Desc", 100.0, "invalid")
