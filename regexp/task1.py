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
            return [i for i in re.findall(RegParser.ADDRESS_REGEX, text, re.MULTILINE)]
        if order == 2:
            res = []
            for pair in [dict(zip(['age', 'name', 'surname', 'city'], v)) for v in
                         re.findall(RegParser.CONTACT_REGEX, text, re.MULTILINE)]:
                res.append({k: v for k, v in pair.items() if v})
            return res

        if order == 3:
            return [float(num.replace(',', '.')) if '.' in num or ',' in num else int(num)
                    for num in re.findall(RegParser.PRICE_REGEX, text, re.MULTILINE)]
