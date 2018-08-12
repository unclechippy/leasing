from django.contrib import admin

from .models import Lease, Charge

admin.site.register(Lease)
admin.site.register(Charge)
