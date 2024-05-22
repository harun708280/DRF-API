from django.contrib import admin
from .models import Company, Employee

class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name', 'location', 'company_id']  # Changed 'id' to 'company_id' as 'id' is not defined in the model

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'id']  # Ensure 'position' matches the field name in the model

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)