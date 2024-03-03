class Product:
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        return self.quantity >= quantity

    def buy(self, quantity):
        if self.check_quantity(quantity):
            self.quantity -= quantity
            return True
        else:
            raise ValueError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        self.products[product] = self.products.get(product, 0) + buy_count

    def remove_product(self, product: Product, remove_count=None):
        if remove_count is None:
            self.products[product] = 0
        elif remove_count > self.products[product]:
            self.products[product] = 0
        else:
            self.products[product] -= remove_count

    def clear(self, product: Product):
        self.products[product] = 0

    def get_total_price(self) -> float:
        total_price = 0
        for product, count in self.products.items():
            total_price = product.price * count

        return total_price

    def buy(self, product: Product):
        for product, buy_product in self.products.items():
            product.buy(buy_product)

        self.clear(product)
