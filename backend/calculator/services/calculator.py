import math
from dataclasses import dataclass


#  Утеплитель
@dataclass
class Insulation:
    name: str
    sheet_area: float
    sheet_volume: float
    sheets_package: int


comfort_20 = Insulation(name="Пеноплэкс комфорт 20мм", sheet_area=0.693, sheet_volume=0.0139, sheets_package=20)
comfort_30 = Insulation(name="Пеноплэкс комфорт 30мм", sheet_area=0.6930769230769231, sheet_volume=0.0208,
                        sheets_package=13)
comfort_40 = Insulation(name="Пеноплэкс комфорт 40мм", sheet_area=0.693, sheet_volume=0.0277, sheets_package=10)
comfort_50 = Insulation(name="Пеноплэкс комфорт 50мм", sheet_area=0.6928571428571429, sheet_volume=0.0347,
                        sheets_package=7)
comfort_100 = Insulation(name="Пеноплэкс комфорт 100мм", sheet_area=0.692, sheet_volume=0.0693, sheets_package=4)

insulations = {
    comfort_20.name: comfort_20,
    comfort_30.name: comfort_30,
    comfort_40.name: comfort_40,
    comfort_50.name: comfort_50,
    comfort_100.name: comfort_100
}


#  Калькулятор
class Calculator:
    def __init__(self, thickness, area, price, insulation: Insulation):
        self.thickness = thickness
        self.area = area
        self.price = price
        self.name = insulation.name
        self.sheet_area = insulation.sheet_area
        self.sheet_volume = insulation.sheet_volume
        self.sheets_packages = insulation.sheets_package

    def calculator(self):
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
