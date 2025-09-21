
from models.restaurants import Restaurant
from models.menu.drink import Drink
from models.menu.food import Food


restaurant_praca = Restaurant("Praça", "Gourmet")
restaurant_pizza = Restaurant("Pizza Speed", "Pizza")

drink = Drink("Suco de Uva", 10, "É muito bom")
food = Food("Macarrão", 50, "É muito bom")

for r in restaurant_pizza.get_rattings():
    print(r)

restaurants = [
    restaurant_praca,
    restaurant_pizza
]


# print(restaurants)
# print(vars(restaurant_praca))
# print(restaurant_praca)

def main():
    Restaurant.get_all_restaurants()

    pass

if __name__ == '__main__':
    main()