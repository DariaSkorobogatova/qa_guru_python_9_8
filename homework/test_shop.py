"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product, demand_quantity=10):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(demand_quantity)

    def test_product_buy(self, product, demand_quantity=10, left_quantity=990):
        # TODO напишите проверки на метод buy
        product.buy(demand_quantity)
        assert product.quantity == left_quantity

    def test_product_buy_more_than_available(self, product, demand_quantity=1100):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(demand_quantity)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_cart_add_product(self, product, cart):
        # TODO напишите проверки на метод check_quantity
        cart.add_product(product)
        cart.add_product(product)
        assert cart.products[product] == 1

