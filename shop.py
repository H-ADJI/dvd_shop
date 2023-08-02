import re
from abc import ABC, abstractmethod


class MarketingStrategy(ABC):
    @abstractmethod
    def apply_sale_strategy(self, products: list[str]) -> float:
        ...


class BackToTheFutureStrategy(MarketingStrategy):
    two_parts_sale = 0.9
    tree_parts_sale = 0.8
    ordinary_dvd_price = 20
    back_to_the_future_price = 15

    def apply_sale_strategy(self, products: list[str]):
        products_number = len(products)
        parts = set()
        for product in products:
            if "back to the future" in product.lower():
                movie_part = re.match(r"\d", product)
                if movie_part:
                    parts.add(int(movie_part))
        bttf_count = len(parts)
        full_price = (products_number - bttf_count) * 20 + bttf_count * 15

        if bttf_count == 2:
            return full_price * self.two_parts_sale
        elif bttf_count > 2:
            return full_price * self.tree_parts_sale
        return full_price


class Cart:
    def __init__(self, products: list[str] = None) -> None:
        self.products = products or []

    def add_dvd(self, dvd_name: str):
        self.products.append(dvd_name)

    def empty_cart(self):
        self.products = []

    @property
    def cart_size(self):
        return len(self.products)

    def payment(self, strategy: MarketingStrategy = None):
        return strategy.apply_sale_strategy(self.products)
