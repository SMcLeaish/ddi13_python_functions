print("Hello neighbors, let's plan a party!")
number_of_guests: int = 12
cost_per_person: float = 3.50
party_location: str = "Mi casita"


class Total_Cost:
    def __init__(self, num: int, cost: float, loc: str):
        self.num: int = num
        self.cost: float = cost
        self.total: float = self.num * self.cost
        self.add_cost: float
        self.loc: str = loc
        self.discount: float = 0.05

    def apply_discount(self):
        self.total = self.total - (self.total * self.discount)

    def print_total(self):
        print(self.total + self.add_cost)

    def print_summary(self):
        print(
            f"We will have {self.num} guests at {self.loc} and the total cost is {self.total:.2f}"
        )


party = Total_Cost(number_of_guests, cost_per_person, party_location)
party.print_total
party.print_summary()
party.apply_discount()
party.print_summary()
