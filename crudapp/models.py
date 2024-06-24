from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    email = models.EmailField(max_length=277, verbose_name="Student Email")
    Phone_No=models.IntegerField(max_length=30,verbose_name="Student phone_No")
    sports=models.CharField(max_length=100,verbose_name="Student sports")
    def __str__(self):
        return str(self.id)
