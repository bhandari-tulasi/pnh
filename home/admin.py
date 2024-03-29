from django.contrib import admin

from .models import Doctor, Staff, Department
# Register your models here.
# admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Staff)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('deptName',)