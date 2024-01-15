import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from calculator.services import Calculator, insulations


# Create your views here.

def index(request):

    return render(request, '../templates/index.html', {'insulations': insulations})


@csrf_exempt
def calculation(request):
    data = json.loads(request.body)

    area = int(data['required_area'])
    price = int(data['package_price'])
    insulation = data['insulation']

    response = Calculator(area, price, insulation=insulations[insulation]).calculator()

    return JsonResponse(response, json_dumps_params={"ensure_ascii": False})
