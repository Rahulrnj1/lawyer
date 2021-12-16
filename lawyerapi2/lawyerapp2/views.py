from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse, JsonResponse
from .models import Departments
from .serializers import Departmentserializer

# Create your views here.

@csrf_exempt
def lawyerapi2(request,id=0):
     if request.method== 'GET':
         departments = Departments.objects.all()
         departments_serializer=Departmentserializer(departments,many=True)
         return JsonResponse(departments_serializer.data,safe=False)
     elif request.method== 'POST':
         department_data=JSONParser().parse(request)
         departments_serializer=Departmentserializer(data=department_data)
         if departments_serializer.is_valid():
             departments_serializer.save()
             return JsonResponse("Added successfully",safe=False)
         return JsonResponse("Failed to Add",safe=False)
     elif request.method== 'PUT':
         department_data=JSONParser().parse(request)
         departments=Departments.objects.get(DepartmentId=department_data['Departmentid'])
         departments_serializer=Departmentserializer(departments,data=department_data)

         if departments_serializer.is_valid():
             departments_serializer.save()
             return JsonResponse("Update successfully",safe=False)
         return JsonResponse("Failed to Update")
     elif request.method=='DELETE':
         departments=Departments.objects.get(DepartmentId=id)
         departments.delete()
         return JsonResponse("Deleted successfully")


