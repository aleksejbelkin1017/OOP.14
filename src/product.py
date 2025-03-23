class Product:
    """ Класс для представления товара. """
    name: str
    description: str
    _price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """ Инициализирует новый экземпляр класса Product. """
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом")
        if not isinstance(quantity, int):
            raise TypeError("Количество должно быть целым числом")

        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        """ Геттер для цены """
        return self._price

    @price.setter
    def price(self, new_price):
        """ Сеттер для цены с проверкой """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self._price:
            # Запрос подтверждения от пользователя
            response = input(f"Цена ниже текущей. Подтвердить изменение? (y/n): ")
            if response.lower() == 'y':
                self._price = new_price
            else:
                print("Изменение цены отменено пользователем")
        else:
            self._price = new_price

    @classmethod
    def new_product(cls, product_data, existing_products=None):
        """
        Создает новый объект Product из словаря с данными
        :param product_data: словарь с параметрами товара
        :param existing_products: список существующих товаров для проверки дубликатов
        :return: объект класса Product
        """
        # Извлекаем параметры из словаря
        name = product_data.get('name')
        description = product_data.get('description')
        price = product_data.get('price')
        quantity = product_data.get('quantity')

        # Если передан список существующих товаров
        if existing_products:
            # Ищем товар с таким же названием
            for existing_product in existing_products:
                if existing_product.name == name:
                    # Если нашли, обновляем количество и цену
                    existing_product.quantity += quantity
                    existing_product.price = max(existing_product.price, price)
                    return existing_product

        # Если товар не найден или список не передан - создаем новый
        return cls(name, description, price, quantity)
