import typing
import functools

DATA = {
    "Vasya": {
        "Mathematics": [1, 6, 3, 8, 3, 4, 3],
        "Russian": [1, 6, 3, 1, 3, 1, 3],
        "Belarussian": [1, 6, 3, 8, 3, 1, 3],
    },
    "Petya": {
        "Esd": [8, 9, 9, 9, 8, 9],
        "Russian": [1, 6, 3, 8, 3, 1, 3],
        "fC": [1, 6, 3, 8, 3, 1, 3],
    }
}


def analyze_students(data: dict) -> set:
    return set((x, y, functools.reduce(lambda el1, el2: el1 + el2, data[x][y])) for x in data.keys() for y in data[x] if y != "1C")


def validate_data(data: dict) -> bool:
    for name in data.keys():
        if not isinstance(name, str):
            raise TypeError
        if not name.isascii() or any(symbol.isdigit() for symbol in name):
            raise ValueError
        for subject in data[name]:
            if not isinstance(subject, str):
                raise TypeError
            if not subject.isascii() or any(symbol.isdigit() for symbol in subject):
                raise ValueError
            for mark in data[name][subject]:
                if isinstance(mark, bool):
                    raise TypeError
                if not isinstance(mark, int):
                    raise TypeError
                if mark > 10 or mark < 1:
                    raise ValueError
    return True


print(analyze_students(DATA))
print(validate_data(DATA))
