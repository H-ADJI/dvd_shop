import pytest

from shop import Cart,BackToTheFutureStrategy

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
            "Back to the Future 3",
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


def test_empty_cart(empty_cart: Cart):
    assert empty_cart.cart_size == 0
    assert empty_cart.products == []


def test_random_cart(random_movies: list[str]):
    my_cart = Cart(products=random_movies)
    assert my_cart.cart_size == len(random_movies)
    assert my_cart.products == random_movies


def test_strategy(normal_cart:Cart):
    startegy = BackToTheFutureStrategy()
    assert normal_cart.payment(strategy=startegy) == normal_cart.cart_size*20

def test_add_products():
    pass


def test_remove_products():
    pass
