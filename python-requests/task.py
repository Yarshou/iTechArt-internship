import typing
import urllib.request as req

import requests
from bs4 import BeautifulSoup

BANK_API_URL = "https://www.nbrb.by/api/exrates/rates?periodicity=0"
WEATHER_URL = "https://yandex.by/pogoda/region/149"


def get_current_exchange_rates(cur_name: str) -> str:
    if cur_name:
        try:
            api_response = requests.get(BANK_API_URL).json()
            currency = [cur for cur in api_response if cur['Cur_Abbreviation'] == cur_name]
            if currency[0]['Cur_Scale'] == 100:
                return f"1 BYN - {round(100 / currency[0]['Cur_OfficialRate'], 2)} {cur_name}"
            else:
                return f"1 BYN - {round(1 / currency[0]['Cur_OfficialRate'], 2)} {cur_name}"
        except IndexError:
            print('Invalid Currency Name')


def get_weather_info() -> typing.Dict[str, int]:
    html = req.urlopen(WEATHER_URL).read()
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='place-list')
    result = {}
    for item in items:
        for letter in item.find('ul').find_all('li'):
            reqs = req.urlopen("https://yandex.by" + letter.find('a').get("href")).read()
            soup2 = BeautifulSoup(reqs, 'html.parser')
            try:
                temp = soup2.find('div', class_="temp fact__temp fact__temp_size_s"). \
                    find('span', class_='temp__value temp__value_with-unit').get_text()
                result[letter.get_text()] = int(temp)
                print(result)
            except AttributeError:
                pass
    return result


print(get_current_exchange_rates("USD"))
print(get_current_exchange_rates("EUR"))
print(get_current_exchange_rates("RUB"))
get_weather_info()
