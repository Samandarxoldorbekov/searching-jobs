from django.db import models
from apps.common.models import TermChoise, JobsType, DegreeChoise, DiplomChoise

class JobsAdd(models.Model):
    jobs_name = models.CharField(max_length=255)
    bio = models.TextField()
    jobs_term = models.CharField(choices=TermChoise.choices, max_length=20)
    logistika = models.CharField(max_length=100)
    degree = models.CharField(choices=DegreeChoise.choices,max_length=30)
    salary = models.IntegerField()
    company_name = models.CharField(max_length=255)
    size_workers = models.IntegerField(name="jami ishchilar soni")
    jobstype = models.CharField(choices=JobsType.choices, max_length=244)
    diplom = models.CharField(choices=DiplomChoise.choices,max_length=122)

