class Country:
    def __init__(self , name, capital, population):
        self.name = name
        self.capital = capital
        self.pop = population

    def get_info(self):
        return{
            'Name': self.name,
            'Capital': self.capital,
            'Population': self.pop
        }

class DevelopedCountry(Country):
    def __init__(self , name, capital, population, gdp):
        super().__init__(name, capital, population)
        self.gdp = gdp

    def get_info(self):
        info = super().get_info()
        info['GDP'] = self.gdp
        return info

class DevelopingCountry(Country):
    def __init__(self , name, capital, population, hdi):
        super().__init__(name, capital, population)
        self.hdi =hdi

    def get_info(self):
        info = super().get_info()
        info["HDI"] = self.hdi
        return info

class World:
    def __init__(self):
        self.countries = []

    def add_country(self, country):
        self.countries.append(country)

    def get_country_info(self, name):
        for country in self.countries:
            if country.name == name:
                return country.get_info()
        return None

world = World()

rsa = DevelopedCountry("South Africa", "Cape Town", 32500142 , 21549871)
china = DevelopingCountry("China" , "Beijing" , 12549875 , 12365478987)
uae = DevelopingCountry("United Emirates" , "Dubai" , 5468754331 , 1236578987445627)

world.add_country(rsa)
world.add_country(china)
world.add_country(uae)

country_info = world.get_country_info('China')

if country_info:
    print("Country, Info:  ")
    for key, value in country_info.items():
        print(f"{key}:{value}")
else:
    print("Country Invalid")
