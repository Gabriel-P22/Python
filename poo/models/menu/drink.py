from models.menu.item_menu import ItemMenu


class Drink(ItemMenu):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self._description = description