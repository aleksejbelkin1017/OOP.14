class Category:
    """ Класс для представления категории товаров. """
    name: str
    description: str
    products: list

    # Атрибуты класса для подсчета
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """ Инициализирует новый экземпляр класса Category. """
        if not isinstance(products, list):
            raise TypeError("Продукты должны быть в виде списка")

        self.name = name
        self.description = description
        self.products = products

        # Увеличение счетчиков при создании новой категории
        Category.category_count += 1
        Category.product_count += len(products)
