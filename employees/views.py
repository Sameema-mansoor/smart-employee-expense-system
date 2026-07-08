from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView

from .models import Employee, Department, Expense
from .serializers import EmployeeSerializer, DepartmentSerializer, ExpenseSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["department", "designation", "status"]
    search_fields = ["first_name", "last_name", "email", "employee_id"]
    ordering_fields = ["salary", "hire_date", "first_name"]


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status", "category"]
    search_fields = ["title", "description"]
    ordering_fields = ["amount", "expense_date"]

    @action(detail=True, methods=["post"])
    def approve(self, request, pk=None):
        expense = self.get_object()
        expense.status = "Approved"
        expense.save()
        return Response({"message": "Expense approved successfully"})

    @action(detail=True, methods=["post"])
    def reject(self, request, pk=None):
        expense = self.get_object()
        expense.status = "Rejected"
        expense.save()
        return Response({"message": "Expense rejected successfully"})
    
class DashboardAPIView(APIView):
    def get(self, request):
        data = {
            "total_employees": Employee.objects.count(),
            "total_departments": Department.objects.count(),
            "total_expenses": Expense.objects.count(),
            "pending_expenses": Expense.objects.filter(status="Pending").count(),
            "approved_expenses": Expense.objects.filter(status="Approved").count(),
            "rejected_expenses": Expense.objects.filter(status="Rejected").count(),
        }

        return Response(data)