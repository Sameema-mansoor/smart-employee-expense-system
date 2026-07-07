from django.contrib import admin
from .models import Employee, Department, Expense


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "employee_id",
        "first_name",
        "last_name",
        "email",
        "department",
        "designation",
        "status",
    )

    search_fields = (
        "employee_id",
        "first_name",
        "last_name",
        "email",
    )

    list_filter = (
        "department",
        "status",
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )

    search_fields = (
        "name",
    )

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("title", "employee", "category", "amount", "status", "expense_date")
    search_fields = ("title", "category", "employee__first_name")
    list_filter = ("status", "category")