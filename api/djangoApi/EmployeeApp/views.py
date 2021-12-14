from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import logging


from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import Departmentserializer, Employeeserializer
logger = logging.getLogger(__name__)


# Create your views here.
@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        Department = Departments.objects.all()
        print(Department)
        print([1,2,3])
        departments_serialzer=Departmentserializer(Department,many=True)   
        print(departments_serialzer)
        return JsonResponse(departments_serialzer.data,safe=False)
        #return JsonResponse([{"name":"Mritunjay"},{"name":"shyam"}],safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serialzer=Departmentserializer(data=department_data)
        if departments_serialzer.is_valid():
            departments_serialzer.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("failed to Add",safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serialzer=Departmentserializer(department,data=department_data,partial=True)
        if departments_serialzer.is_valid():
            departments_serialzer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        department_data=JSONParser().parse(request)
        Department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        Department.delete()
        return JsonResponse("Deleted Successfully",safe=False)

    

