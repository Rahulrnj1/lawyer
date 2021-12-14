from rest_framework import fields, serializers
from .models import Departments,Employees
#from djangoApi.EmployeeApp.models import Departments

class Departmentserializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId','DepartmentName')

class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId','EmployeeName','Department','dateOfjoining','photoFileName')