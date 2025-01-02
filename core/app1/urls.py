from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='barangay-home'),

    path('residents/', views.residents, name='barangay-residents'),
    path('add-resident/', views.add_resident, name='add-barangay-resident'),
    path('update-resident/<int:pk>/', views.update_resident, name='update-barangay-resident'),
    path('delete-resident/<int:pk>/', views.delete_resident, name='delete-barangay-resident'),

    path('medicine-inventory/', views.medicine_inventory, name='barangay-medicine-inventory'),
    path('add-medicine/', views.add_medicine, name='barangay-add-medicine'),
    path('update-medicine/<int:pk>/', views.update_medicine, name='barangay-update-medicine'),
    path('delete-medicine/<int:pk>/', views.delete_medicine, name='barangay-delete-medicine'),
    
    path('medicine-request/', views.medicine_request, name='barangay-medicine-request'),
    path('medicine-request-history/', views.medicine_request_history, name='barangay-medicine-request-history'),

    path('children-list/', views.children_list, name='children-list'),
    path('update-visit/<int:pk>/', views.update_visit, name='update-visit'),
    path('child-vaccine-history/<int:pk>/', views.visit_history, name='child-vaccine-history'),
]