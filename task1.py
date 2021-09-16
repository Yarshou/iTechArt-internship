import fractions
import decimal
import collections
import typing


def get_max_and_min(data: typing.Union[float, fractions.Fraction, str]) -> tuple:
    data = list(data)
    for elem in enumerate(data):
        if isinstance(elem[1], str):
            try:
                data[elem[0]] = float(data[elem[0]])
            except ValueError:
                data[elem[0]] = fractions.Fraction(elem[1].replace(" ", "").replace("\\", "/"))
    Point = collections.namedtuple('Point', ['min_value', 'max_value'])
    p = Point(min_value=min(data), max_value=max(data))
    return p


print(get_max_and_min({5 / 124, '123.123', '4 \ 9'}))
print(get_max_and_min({5 / 6, '123.123', '4 \ 9'}).min_value)
print(get_max_and_min({5 / 6, '123.123', '4 \ 9'}).max_value)
