from models.rating import Rating

class Restaurant:    
    restaurants = []

    def __init__(self, name, category):
            self.name = name
            self.category = category
            self._active = False
            self._rating = []
            Restaurant.restaurants.append(self)
    
    def __str__(self):
          return f"{self.name} | {self.category} | {self._active}"
    
    def get_all_restaurants():
          for r in Restaurant.restaurants:
                print(r)

    def add_rating(self, rating: Rating):
          self._rating.append(rating)
    
    def get_rattings(self):
          return self._rating
    
    @property
    def get_average(self):
          if not self._rating:
            return 0
          
          sum_rates = sum(r.get_score() for r in self._rating)
          all_rates = len(self._rating)

          return round(sum_rates / all_rates, 1)

    @property
    def active(self):
        return "Active" if (self.active) else "Inactive"
                
