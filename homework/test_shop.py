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

    def test_cart_add_the_same_product(self, product, cart):
        cart.add_product(product)
        cart.add_product(product)
        cart.add_product(product)
        assert cart.products[product] == 3

    def test_cart_add_the_same_product_dif_buy_count(self, product, cart):
        cart.add_product(product, buy_count=75)
        assert cart.products[product] == 75

    def test_cart_add_different_products(self, cart):
        product1 = Product("book", 100, "This is a book", 1000)
        product2 = Product("chocolate", 158, "This is a delicious bar", 2057)
        cart.add_product(product1)
        cart.add_product(product2)
        assert len(cart.products) == 2
        assert cart.products[product1] == 1
        assert cart.products[product2] == 1

    def test_cart_remove_product_no_remove_count(self, product, cart):
        cart.add_product(product)
        cart.remove_product(product)
        assert len(cart.products) == 0

    def test_cart_remove_product_with_remove_count_less_than_quantity(
        self, product, cart
    ):
        cart.add_product(product, buy_count=5)
        cart.remove_product(product, remove_count=1)
        assert cart.products[product] == 4

    def test_cart_remove_product_with_remove_count_more_than_quantity(
        self, product, cart
    ):
        cart.add_product(product, buy_count=64)
        cart.remove_product(product, remove_count=65)
        assert len(cart.products) == 0

    def test_cart_clear(self, product, cart):
        cart.add_product(product, buy_count=100)
        cart.clear()
        assert len(cart.products) == 0

    def test_cart_get_total_price(self, product, cart):
        cart.add_product(product, buy_count=36)
        assert cart.get_total_price() == 3600

    def test_cart_buy_quantity_is_enough(self, product, cart):
        cart.add_product(product, buy_count=3)
        cart.buy()
        assert product.quantity == 997
        assert len(cart.products) == 0

    def test_cart_buy_quantity_is_not_enough(self, product, cart):
        cart.add_product(product, buy_count=1001)
        with pytest.raises(ValueError):
            assert cart.buy()
