"""leases URL Configuration

"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('new', views.new_lease, name='new_lease'),
    path('<int:pk>', views.DetailView.as_view(), name='lease'),
    path('<int:charge_id>', views.charge, name='charge')
]
