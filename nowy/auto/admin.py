from django.contrib import admin
from .models import Car, Lender, Hire
# Register your models here.

admin.site.register(Car)
admin.site.register(Hire)
admin.site.register(Lender)
