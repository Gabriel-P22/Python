
from models.restaurants import Restaurant
from models.rating import Rating


restaurant_praca = Restaurant("Praça", "Gourmet")
restaurant_pizza = Restaurant("Pizza Speed", "Pizza")
restaurant_pizza.add_rating(Rating("Customer_1", 1))

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