from django.contrib import admin
from .models import Auto,Lender, Hire
# Register your models here.

admin.site.register(Auto)
admin.site.register(Hire)
admin.site.register(Lender)

