class Travel:
    def __init__(self, country, month, type):
        self.country = country
        self.month = int(month)
        self.type = type
        self.price = 0

    def trip_info(self):
        if self.month >= 2 and self.month <= 6:
            print(f"you are going to {self.country} in the Winter! this is a {self.type} ")
        elif self.month > 6 and self.month  < 12:
            print(f" You are going to a {self.country} in the Summer! this is a {self.type} trip")
        else:
            print("invalid input")

    def calc_cost(self , cost):
        costs = []
        while cost != 0:
            self.price += cost
            costs.append(cost)
            cost = int(input("Enter another cost"))

        advice = self.advice(self.price)
        inspect = self.list_inspect(costs)
        return advice, inspect

    def advice(self, num):
        if num < 500:
            print(" Low Budget Room")
        elif num >= 500 and num < 1500:
            print("Luxury Room")
        else:
            print("Luxury Trip")

    def list_inspect(self, costs):
        less_than_ten = 0
        for i in costs:
            if i >= 10:
                less_than_ten += 1

        if less_than_ten <= 10:
            self.price += 100
            print(f"Updated Price : {self.price}")

location = input("Enter a country:  ").capitalize()
trip_type = input("Leisure or Business:  ").capitalize()
month = input("Enter a month:  ")

test = Travel(location, month, trip_type)
test.trip_info()

flight_cost = int(input("Enter flight price"))
test.calc_cost(flight_cost)







