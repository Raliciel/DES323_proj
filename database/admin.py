from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(HR_description)
class HR_descriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(HR_department)
class HR_departmentAdmin(admin.ModelAdmin):
    pass


@admin.register(setting)
class settingAdmin(admin.ModelAdmin):
    pass