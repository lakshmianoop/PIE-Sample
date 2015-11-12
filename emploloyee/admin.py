from django.contrib import admin
from .models import Employee
from .models import Department

admin.site.register(Department)
admin.site.register(Employee)


# Register your models here.
