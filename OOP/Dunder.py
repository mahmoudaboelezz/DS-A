#overloading len()

class Order:
    def __init__(self,cart,customer):
        self.cart = cart
        self.customer = customer

    # def get_cart_len(self):
    #     return len(self.cart)

    def __len__(self):
        return len(self.cart)

    #allow you to call object name without error
    def __call__(self):
        print(f"{self.customer}")


order = Order(["Laptop", "monitor"], "islam")
# print(order.get_cart_len())
print(len(order))
order()