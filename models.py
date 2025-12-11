from django.db import models

# Create your models here.
class Admin(models.Model):
    name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=20)
    gender_choices=[('M','male'),('F','female')]
    gender=models.CharField(max_length=1,choices=gender_choices)
    hall_ticket_number=models.CharField(max_length=10)
    branch_choices=[('ECE','ECE'),('CSE','CSE'),('EEE','EEE'),('AIML','AIML'),('AIDS','AIDS')]
    branch=models.CharField(max_length=10,choices=branch_choices)
    college=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Marks(models.Model):
    hall_ticket_number=models.CharField(max_length=10)
    m1=models.IntegerField()
    physics=models.IntegerField()
    chemistry=models.IntegerField()
    english=models.IntegerField()
    drawing=models.IntegerField()