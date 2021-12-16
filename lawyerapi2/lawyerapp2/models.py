from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentId = models.IntegerField(primary_key=True)
    DepartmentName = models.CharField(max_length=500,)
    Departmentmail = models.EmailField()
    Departmentsection = models.CharField(max_length=120)
    Departmentdetails = models.TextField()
    DepartmentType = models.TextField()
