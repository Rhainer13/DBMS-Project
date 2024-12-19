from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='barangay-home'),

    path('residents/', views.residents, name='barangay-residents'),
    path('add-resident/', views.add_resident, name='add-barangay-resident'),
    path('update-resident/<int:pk>/', views.update_resident, name='update-barangay-resident'),
]