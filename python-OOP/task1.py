import typing


class Department:
    class BudgetError(ValueError):
        pass

    def __init__(self, name: str, employees: typing.Dict[str, float], budget: int):
        self.name = name
        self.employees = employees
        self.budget = budget

    def __str__(self):
        return f"{self.name} ({len(self.employees.keys())} - {self.average_salary}, {self.budget})"

    def __or__(self, other):
        self_plan = self.get_budget_plan()
        other_plan = other.get_budget_plan()
        return self if self_plan > other_plan or self_plan == other_plan else other

    def __add__(self, other):
        return self.merge_departments(self, other)

    def get_budget_plan(self) -> float:
        budg = self.budget - sum(self.employees.values())
        if budg < 0:
            raise self.BudgetError
        return budg

    @property
    def average_salary(self) -> float:
        return round(sum(self.employees.values()) / len(self.employees.keys()), 2)

    @staticmethod
    def merge_departments(*args):
        employees = {}
        budget = 0
        dep_dict = {}
        for dep in args:
            dep_dict[dep.name] = dep.average_salary
            budget += dep.budget
            employees = {k: v for k, v in dep.employees.items()}
        sorted_names = dict(sorted(dep_dict.items(), key=lambda x: (-x[1], x[0])))
        new_dep = Department(" - ".join(sorted_names.keys()), employees, budget)
        new_dep.get_budget_plan()
        return new_dep
