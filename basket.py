class ShoppingBasket:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False
       
    def login(self, input_username, input_password):
        if input_username == self.username and input_password == self.password:
            self.logged_in = True
            print("Вы вошли в корзину.")
        else:
            print("Invalid username or password.")

cart = ShoppingBasket("example_user", "password123")
cart.login("example_user", "password123")

