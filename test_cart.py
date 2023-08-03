import pytest

from shop import BackToTheFutureStrategy, Cart


@pytest.fixture
def random_movies():
    return [
        "Back to the Future 1",
        "Back to the Future 2",
        "The Way Back",
        "Oppenheimer",
    ]


@pytest.fixture
def empty_cart():
    return Cart()


@pytest.fixture
def special_cart_1():
    return Cart(
        [
            "Back to the Future 1",
            "Back to the Future 2",
        ]
    )


@pytest.fixture
def special_cart_2():
    return Cart(
        [
            "Back to the Future 1",
            "Back to the Future 2",
            "Back to the Future 3",
        ]
    )


@pytest.fixture
def normal_cart():
    return Cart(
        [
            "The Way Back",
            "Oppenheimer",
        ]
    )


def test_empty_cart(normal_cart: Cart, empty_cart: Cart):
    assert empty_cart.is_empty
    assert empty_cart.cart_size == 0
    assert empty_cart.products == []

    assert normal_cart.is_empty is False
    assert normal_cart.cart_size > 0
    normal_cart.empty_cart()
    assert normal_cart.cart_size == 0
    assert normal_cart.products == []


def test_random_cart(random_movies: list[str]):
    my_cart = Cart(products=random_movies)
    assert my_cart.cart_size == len(random_movies)
    assert my_cart.products == random_movies


def test_strategy(normal_cart: Cart, special_cart_1: Cart, special_cart_2: Cart):
    startegy = BackToTheFutureStrategy()
    assert normal_cart.price(strategy=startegy) == normal_cart.cart_size * 20
    assert (
        special_cart_1.price(strategy=startegy)
        == (
            (special_cart_1.cart_size - 2) * startegy.ordinary_dvd_price
            + 2 * startegy.back_to_the_future_price
        )
        * startegy.two_parts_sale
    )
    assert (
        special_cart_2.price(strategy=startegy)
        == (
            (special_cart_2.cart_size - 3) * startegy.ordinary_dvd_price
            + 3 * startegy.back_to_the_future_price
        )
        * startegy.tree_parts_sale
    )


def test_add_products(empty_cart: Cart):
    assert empty_cart.is_empty
    empty_cart.add_dvd("back to the future 5")
    empty_cart.add_dvd("Barbie")
    assert empty_cart.cart_size == 2
