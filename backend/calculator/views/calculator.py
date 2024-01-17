import json
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import ListView
from django.views import View

from calculator.models import Insulation
from calculator.services import Calculator


# Create your views here.


@method_decorator(csrf_exempt, name="dispatch")
class InsulationListView(ListView):
    template_name = '../templates/index.html'
    model = Insulation
    context_object_name = 'insulations'

    def get_queryset(self):
        insulations = self.model.objects.all()
        return insulations


@method_decorator(csrf_exempt, name="dispatch")
class CalculateView(View):
    model = Insulation
    fields = ['sheet_area', 'sheet_volume', 'sheets_package']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        insulation_id = data['id']
        area = data['area']
        price = data['price']

        obj = self.model.objects.get(pk=insulation_id)

        response = Calculator(
            area,
            price,
            insulation=Insulation(
                sheet_area=obj.sheet_area,
                sheet_volume=obj.sheet_volume,
                sheets_package=obj.sheets_package
            )
        ).calculate()

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})
