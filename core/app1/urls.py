from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='barangay-home'),

    path('residents/', views.residents, name='barangay-residents'),
]