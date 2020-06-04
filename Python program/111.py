# define a basic city class
class City:
    def __init__(self, name, country, elevation, population):
        self.name = name
        self.country = country
        self.elevation = elevation
        self.population = population
# create a new instance of the City class and
# define each attribute
city1 = City("Cusco","Peru",3399,358052)
# create a new instance of the City class and
# define each attribute
city2 = City("Sofia","Bulgaria",2290,1241675)
# create a new instance of the City class and
# define each attribute
city3 = City("Seoul","South Korea",38,9733509)
def max_elevation_city(min_population):
# Initialize the variable that will hold
# the information of the city with
# the highest elevation
    cities = [city1, city2, city3]
    lowest = None
    lowest_pop = 999999999
    for city in cities:
        if city.population >= min_population:
            if city.population <= lowest_pop:
                lowest = city
    if lowest != None:
        return lowest.name, lowest.country
    return ""
print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""