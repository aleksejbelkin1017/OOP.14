from src.product import Product

class Category:
    """ Класс для представления категории товаров. """
    name: str
    description: str
    _products: list

    # Атрибуты класса для подсчета
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """ Инициализирует новый экземпляр класса Category. """
        if not isinstance(products, list):
            raise TypeError("Продукты должны быть в виде списка")

        self.name = name
        self.description = description
        self._products = products
        print(f"Инициализированные продукты: {[f'{product.name}, {product.price} руб., {product.quantity} шт.' for product in self._products]}")

        # Увеличение счетчиков при создании новой категории
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """ Метод добавляет продукт в категорию """
        print(f"Продукты до добавления: {[f'{product.name}, {product.price} руб., {product.quantity} шт.' for product in self._products]}")
        if not isinstance(product, Product):
            raise TypeError("Продукт должен быть объектом класса Product")
        self._products.append(product)
        print(f"Продукты после добавления: {[f'{product.name}, {product.price} руб., {product.quantity} шт.' for product in self._products]}")
        Category.product_count += 1

    @property
    def products(self):
        product_list = []
        for product in self._products:
            product_info = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            product_list.append(product_info)
        return "\n".join(product_list)

# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     print(category1.products)
#     product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
#     category1.add_product(product4)
#     print(category1.products)
#     print(category1.product_count)
#
#     new_product = Product.new_product(
#         {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#          "quantity": 5})
#     print(new_product.name)
#     print(new_product.description)
#     print(new_product.price)
#     print(new_product.quantity)
#
#     new_product.price = 800
#     print(new_product.price)
#
#     new_product.price = -100
#     print(new_product.price)
#     new_product.price = 0
#     print(new_product.price)