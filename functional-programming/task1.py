import fractions
import decimal
import collections
import typing

Point = collections.namedtuple('Point', ['max_value', 'min_value'])


def get_max_and_min(data: typing.Set[typing.Union[fractions.Fraction, decimal.Decimal, str]]) -> tuple:
    for elem in enumerate(data):
        if isinstance(elem[1], str):
            try:
                data[elem[0]] = decimal.Decimal(data[elem[0]])
            except decimal.InvalidOperation:
                data[elem[0]] = fractions.Fraction(elem[1].replace(" ", "").replace("\\", "/"))
    p = Point(max_value=max(data), min_value=min(data))
    return p
