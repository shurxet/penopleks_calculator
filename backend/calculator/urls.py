from django.urls import path
from calculator import views

urlpatterns = [
    path('', views.InsulationListView.as_view(), name='InsulationListView'),
    path('calculation', views.CalculateView.as_view(), name='CalculateView')
]
