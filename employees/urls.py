from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet, ExpenseViewSet

router = DefaultRouter()

router.register("employees", EmployeeViewSet)
router.register("departments", DepartmentViewSet)
router.register("expenses", ExpenseViewSet)

urlpatterns = [
    path("", include(router.urls)),

]