from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PartyPlan:
    num: int
    cost: float
    loc: str
    disc: float | None
    add_cost: float | None

    @property
    def total(self) -> float:
        return self.num * self.cost

    @property
    def total_after_discount(self) -> float:
        total_cost = self.total
        return (self.disc and total_cost - (total_cost * self.disc)) or total_cost

    @property
    def summary_total(self) -> float | None:
        return self.total_after_discount + (self.add_cost or 0)


def print_party_summary(
    num: int,
    cost: float,
    loc: str,
    disc: float | None = None,
    add_cost: float | None = None,
) -> None:
    party_plan = PartyPlan(num, cost, loc, disc, add_cost)
    print(
        f"We will have {party_plan.num} guests at {party_plan.loc} and the total cost is {party_plan.summary_total:.2f}"
    )


print("Hello neighbors, let's plan a party!")
print_party_summary(num=15, cost=13.75, loc="Mi Casita")
