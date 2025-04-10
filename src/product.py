from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """ Абстрактный базовый класс для всех продуктов """

    @property
    @abstractmethod
    def price(self):
        """ Геттер для цены """
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        """ Сеттер для цены с проверкой """
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(BaseProduct):
    """ Класс для представления товара. """
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity, color=None):
        """ Инициализирует новый экземпляр класса Product. """
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом")
        if not isinstance(quantity, int):
            raise TypeError("Количество должно быть целым числом")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

    @property
    def price(self):
        """ Геттер для цены """
        return self.__price

    @price.setter
    def price(self, new_price):
        """ Сеттер для цены с проверкой """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            # Запрос подтверждения от пользователя
            response = input("Цена ниже текущей. Подтвердить изменение? (y/n): ")
            if response.lower() == 'y':
                self.__price = new_price
            else:
                print("Изменение цены отменено пользователем")
        else:
            self.__price = new_price

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

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        # Проверяем, что other является объектом Product
        if not isinstance(other, Product):
            if isinstance(other, (int, float)):
                # Если other - число, возвращаем общую стоимость с добавленной суммой
                return self.price * self.quantity + other
            else:
                raise TypeError("Нельзя складывать продукт с объектом другого типа")

        # Проверяем, что классы продуктов совпадают
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного типа")

        # Если все проверки пройдены, возвращаем сумму стоимостей
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period
