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
        if self_plan > other_plan:
            return self
        elif self_plan == other_plan:
            return self
        else:
            return other

    def __add__(self, other):
        return self.merge_departments(self, other)

    def get_budget_plan(self) -> float:
        budg = self.budget
        for employee in self.employees.keys():
            budg -= self.employees[employee]
            if budg < 0:
                raise self.BudgetError
        return budg

    @property
    def average_salary(self) -> float:
        salary = sum(self.employees.values())
        return round(salary / len(self.employees.keys()), 2)

    @staticmethod
    def merge_departments(*args):
        new_dep = Department("", {}, 0)
        dep_dict = {}
        for dep in args:
            dep_dict[dep.name] = dep.average_salary
            new_dep.budget += dep.budget
            for name, salary in dep.employees.items():
                new_dep.employees[name] = salary
        new_dep.get_budget_plan()
        employees = dict(sorted(dep_dict.items(), key=lambda x: (-x[1], x[0])))
        new_dep.name = " - ".join(employees.keys())
        return new_dep
