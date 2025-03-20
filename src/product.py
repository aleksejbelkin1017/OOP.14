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
