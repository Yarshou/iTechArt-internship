import fractions
import decimal
import collections
import typing

Point = collections.namedtuple('Point', ['max_value', 'min_value'])


def get_max_and_min(data: typing.Set[typing.Union[fractions.Fraction, decimal.Decimal, str]]) -> tuple:
    for elem in data:
        if isinstance(elem, str):
            try:
                data.add(decimal.Decimal(elem))
                data.remove(elem)
            except decimal.InvalidOperation:
                data.add(fractions.Fraction(elem.replace(" ", "").replace("\\", "/")))
                data.remove(elem)

    p = Point(max_value=max(data), min_value=min(data))
    return p