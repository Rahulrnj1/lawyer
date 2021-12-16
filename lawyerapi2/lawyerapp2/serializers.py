from rest_framework import serializers
from .models import Departments 

class Departmentserializer(serializers.ModelSerializer):
     class Meta:
         model = Departments
         fields = ('DepartmentId','DepartmentName','Departmentmail','Departmentsection',
         'Departmentdetails','DepartmentType')