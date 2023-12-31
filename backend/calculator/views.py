from django.shortcuts import render
import math

from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    return render(request, '../templates/index.html')


@csrf_exempt
def calculation(request):

    area = int(request.POST['required_area'])
    thickness = int(request.POST['sheet_thickness'])
    price = int(request.POST['package_price'])

    if thickness == 20:
        sheet_area = 0.693
        number_sheets = math.ceil(area / sheet_area)
        number_packages = number_sheets / 20
        number_sheets_plus = number_sheets - 20 * math.floor(number_packages)
        total_price = price / 20 * number_sheets
        return render(request, '../templates/calculation.html',
                      {
                          'number_sheets': number_sheets,
                          'number_packages': math.floor(number_packages),
                          'number_sheets_plus': number_sheets_plus,
                          'total_price': round(total_price)
                      }
                      )

    elif thickness == 30:
        sheet_area = 0.693
        number_sheets = math.ceil(area / sheet_area)
        number_packages = number_sheets / 13
        number_sheets_plus = number_sheets - 13 * math.floor(number_packages)
        total_price = price / 13 * number_sheets
        return render(request, '../templates/calculation.html',
                      {
                          'number_sheets': number_sheets,
                          'number_packages': math.floor(number_packages),
                          'number_sheets_plus': number_sheets_plus,
                          'total_price': round(total_price)
                      }
                      )

    elif thickness == 40:
        sheet_area = 0.693
        number_sheets = math.ceil(area / sheet_area)
        number_packages = number_sheets / 10
        number_sheets_plus = number_sheets - 10 * math.floor(number_packages)
        total_price = price / 10 * number_sheets
        return render(request, '../templates/calculation.html',
                      {
                          'number_sheets': number_sheets,
                          'number_packages': math.floor(number_packages),
                          'number_sheets_plus': number_sheets_plus,
                          'total_price': round(total_price)
                      }
                      )

    elif thickness == 50:
        sheet_area = 0.692
        number_sheets = math.ceil(area / sheet_area)
        number_packages = number_sheets / 7
        number_sheets_plus = number_sheets - 7 * math.floor(number_packages)
        total_price = price / 7 * number_sheets
        return render(request, '../templates/calculation.html',
                      {
                          'number_sheets': number_sheets,
                          'number_packages': math.floor(number_packages),
                          'number_sheets_plus': number_sheets_plus,
                          'total_price': round(total_price)
                      }
                      )

    elif thickness == 100:
        sheet_area = 0.692
        number_sheets = math.ceil(area / sheet_area)
        number_packages = number_sheets / 4
        number_sheets_plus = number_sheets - 4 * math.floor(number_packages)
        total_price = price / 4 * number_sheets
        return render(request, '../templates/calculation.html',
                      {
                          'number_sheets': number_sheets,
                          'number_packages': math.floor(number_packages),
                          'number_sheets_plus': number_sheets_plus,
                          'total_price': round(total_price)
                      }
                      )
    else:
        return render(request, '../templates/calculation.html',
                      {
                          'absence': 'Нет таких толщин'
                      }
                      )
