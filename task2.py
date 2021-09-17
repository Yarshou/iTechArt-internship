import functools


def analyze_students(data: dict) -> set:
    return set((x, y, functools.reduce(lambda el1, el2: el1 * el2, data[x][y])) for x in data.keys() for y in data[x] if
               y != "1C")


def validate_data(data: dict) -> bool:
    for name in data.keys():
        if not isinstance(name, str):
            raise TypeError
        if not name.isascii() or not name.isalpha() or not name.isalnum():
            raise ValueError
        for subject in data[name]:
            if subject == "1C":
                continue
            if not isinstance(subject, str):
                raise TypeError
            if not subject.isascii() or not subject.isalpha() or not subject.isalnum():
                raise ValueError
            for mark in data[name][subject]:
                if isinstance(mark, bool):
                    raise TypeError
                if not isinstance(mark, int):
                    raise TypeError
                if mark > 10 or mark < 1:
                    raise ValueError
    return True
