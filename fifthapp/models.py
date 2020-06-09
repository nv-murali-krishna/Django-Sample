from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField()
    b_choices=(
    ('M.C.A','M.C.A'),
    ('M.B.A','M.B.A'),
    ('C.S.E','C.S.E'),
    ('E.E.E','E.E.E'),
    ('E.C.E','E.C.E'),
    ('IT','IT'),
    ('CIVL','CIVL'),

    )
    branch=models.CharField(max_length=5, choices=b_choices)
    year=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=20)
