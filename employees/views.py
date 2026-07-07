from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Employee, Department, Expense
from .serializers import EmployeeSerializer, DepartmentSerializer, ExpenseSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

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