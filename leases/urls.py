"""leases URL Configuration

"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:lease_id>', views.lease, name='lease'),
    path('<int:charge_id>', views.charge, name='charge')
]
