import math
from dataclasses import dataclass


#  Утеплитель
@dataclass
class Insulation:
    sheet_area: float
    sheet_volume: float
    sheets_package: int


#  Калькулятор
class Calculator:
    def __init__(self, area, price, insulation: Insulation):
        self.area = area
        self.price = price
        self.sheet_area = insulation.sheet_area
        self.sheet_volume = insulation.sheet_volume
        self.sheets_packages = insulation.sheets_package

    def calculate(self):
        try:
            number_sheets = math.ceil(self.area / self.sheet_area)
            number_packages = number_sheets / self.sheets_packages
            number_sheets_plus = number_sheets - self.sheets_packages * math.floor(number_packages)
            total_volume = self.sheet_volume * number_sheets
            total_price = self.price / self.sheets_packages * number_sheets
            pennies = 0
            rubles = 0

            if type(total_price) is float:
                data = str(round(total_price, 2)).split('.')
                res_rubles = int(data.pop(0))
                res_pennies = int(data.pop())
                pennies += res_pennies
                rubles += res_rubles
            else:
                rubles += total_price

            response = {
                'number_sheets': number_sheets,
                'number_packages': math.floor(number_packages),
                'number_sheets_plus': number_sheets_plus,
                'total_volume': round(total_volume, 5),
                'rubles': rubles,
                'pennies': pennies
            }

            return response
        except ZeroDivisionError:
            abort_message = 'Data type error'
            return {'abort_message': abort_message}
