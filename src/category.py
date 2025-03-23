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
        print(f"Инициализированные продукты: {[f'{product.name}, {product.price} руб., '
                                               f'{product.quantity} шт.' for product in self._products]}")

        # Увеличение счетчиков при создании новой категории
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """ Метод добавляет продукт в категорию """
        print(f"Продукты до добавления: {[f'{product.name}, {product.price} руб., '
                                          f'{product.quantity} шт.' for product in self._products]}")
        if not isinstance(product, Product):
            raise TypeError("Продукт должен быть объектом класса Product")
        self._products.append(product)
        print(f"Продукты после добавления: {[f'{product.name}, {product.price} руб., '
                                             f'{product.quantity} шт.' for product in self._products]}")
        Category.product_count += 1

    @property
    def products(self):
        product_list = []
        for product in self._products:
            product_info = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            product_list.append(product_info)
        return "\n".join(product_list)
