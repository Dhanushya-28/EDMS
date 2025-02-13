from django.db import models

class Department(models.Model):
    departmentId = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=30)


class Employees(models.Model):
    name = models.CharField(max_length=40)
    contactNumber = models.IntegerField()
    qualification = models.CharField(max_length=80)
    emailId = models.EmailField()
    location = models.CharField(max_length=60)
    dateOfJoin = models.DateField()
    createdDateTime = models.DateTimeField(auto_now_add=True)
    departmentId = models.ForeignKey(Department,
                                   on_delete=models.CASCADE,
                                   related_name='api')
   
   
