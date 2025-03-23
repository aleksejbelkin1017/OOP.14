from unittest.mock import patch

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


def test_private_price(product):
    # Проверка, что нельзя напрямую обратиться к _price
    assert product._price is not None  # Проверяем, что атрибут существует


def test_getter(product):
    # Проверка геттера
    assert product.price == 210000.0


def test_setter_positive(product):
    # Проверка установки положительной цены
    product.price = 220000.0
    assert product.price == 220000.0


def test_setter_negative(product):
    # Проверка установки отрицательной цены
    with patch('sys.stdout') as mock_stdout:
        product.price = -100
        captured_output = mock_stdout.write.call_args_list[0][0][0]
        assert "Цена не должна быть нулевая или отрицательная" in captured_output
        assert product.price == 210000.0  # Цена не изменилась


def test_setter_zero(product):
    # Проверка установки нулевой цены
    with patch('sys.stdout') as mock_stdout:
        product.price = 0
        captured_output = mock_stdout.write.call_args_list[0][0][0]
        assert "Цена не должна быть нулевая или отрицательная" in captured_output
        assert product.price == 210000.0  # Цена не изменилась


def test_setter_lower_price_reject(product):
    # Проверка понижения цены с отказом
    with patch('builtins.input', return_value='n'):
        product.price = 200000.0
    assert product.price == 210000.0  # Цена не изменилась


def test_setter_lower_price_accept(product):
    # Проверка понижения цены с подтверждением
    with patch('builtins.input', return_value='y'):
        product.price = 200000.0
    assert product.price == 200000.0  # Цена изменилась


def test_new_product_unique():
    # Проверка создания нового уникального товара
    new_product_data = {
        "name": "Samsung Galaxy S23",
        "description": "256GB, Black",
        "price": 180000.0,
        "quantity": 5
    }
    new_product = Product.new_product(new_product_data)
    assert new_product.name == "Samsung Galaxy S23"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_new_product_duplicate():
    # Создаем список существующих товаров
    existing_products = [Product("iPhone 15", "512GB, Gray space", 210000.0, 8)]
    duplicate_data = {
        "name": "iPhone 15",
        "description": "512GB, Gray space",
        "price": 200000.0,
        "quantity": 3
    }
    result = Product.new_product(duplicate_data, existing_products)
    assert result == existing_products[0]  # Должен вернуть существующий объект
    assert existing_products[0].quantity == 11  # Количество должно суммироваться
    assert existing_products[0].price == 210000.0  # Цена должна обновиться на максимальную
