class Product:
    """ Класс для представления товара. """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """ Инициализирует новый экземпляр класса Product. """
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом")
        if not isinstance(quantity, int):
            raise TypeError("Количество должно быть целым числом")

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data):
        """
        Создает новый объект Product из словаря с данными
        :param product_data: словарь с параметрами товара
        :return: объект класса Product
        """
        # Извлекаем параметры из словаря
        name = product_data.get('name')
        description = product_data.get('description')
        price = product_data.get('price')
        quantity = product_data.get('quantity')

        # Создаем новый объект через конструктор
        return cls(name, description, price, quantity)
