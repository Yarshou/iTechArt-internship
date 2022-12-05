import typing
import re


class RegParser:
    ADDRESS_REGEX = \
        r'^(?:[A-Z][a-z]*, )?(?:[A-Z][a-z]*(?: [Cc]ity)?, )?(?:[A-z \d_-]*(?: str\.)?, )(?:\d+ *[-,/\\|]? *\d+)$'

    CONTACT_REGEX = r'^(?:(?:(?:(?:;)?age=(?P<age>(?:[\d\w -])+))|(?:(?:;)?name=(?P<name>(?:[\d\w -])+))|' \
                    r'(?:(?:;)?surname=(?P<surname>(?:[\d\w -])+))|(?:(?:;)?city=(?P<city>(?:[\d\w -])+)))){1,4}$'

    PRICE_REGEX = r'(?:(?<=(?:[$€]) {1})(?:[\d]+[/.,]?[\d]+))|(?:[\d]+[/.,]?[\d]+)(?=(?: )*BYN)'

    @classmethod
    def find(cls, text: str, order: int) -> typing.List[typing.Union[str, dict, int, float]]:
        if order == 1:
            return re.findall(RegParser.ADDRESS_REGEX, text, re.MULTILINE)
        if order == 2:
            return [match.groupdict() for match in re.finditer(RegParser.CONTACT_REGEX, text, re.MULTILINE)]

        if order == 3:
            return [float(num.replace(',', '.')) if '.' in num or ',' in num else int(num)
                    for num in re.findall(RegParser.PRICE_REGEX, text, re.MULTILINE)]
