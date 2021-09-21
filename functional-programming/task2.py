import typing
import functools

DATA = {
    'Anton': {
        'Python': [10, 10, 10],
        'Django': [10, 10, 10, 10],
    },
    'Alex': {
        'C': [9, 9],
        'Java': [8, 8, 10],
        'Assembler': [7]
    },
    'Loki': {
        '1C': [10, 10, 10, 10, 10],
        'Ruby': [10, 10, 10, 10, 10]
    }
}


def analyze_students(data: dict) -> set:
    return set((x, y, functools.reduce(lambda el1, el2: el1 * el2, data[x][y])) for x in data.keys() for y in data[x] if
               y != "1C")


def validate_data(data: dict) -> bool:
    for name in data.keys():
        if not isinstance(name, str):
            raise TypeError
        if not name.isascii() or not name.isalpha():
            raise ValueError
        for subject in data[name]:
            if subject == "1C":
                continue
            if not isinstance(subject, str):
                raise TypeError
            if not subject.isascii() or not subject.isalpha():
                raise ValueError
            if any(map(lambda x: isinstance(x, bool), data[name][subject])):
                raise TypeError
            if any(map(lambda x: not isinstance(x, int), data[name][subject])):
                raise TypeError
            if any(map(lambda x: x > 10 or x < 1, data[name][subject])):
                raise ValueError
    return True


print(validate_data(DATA))
