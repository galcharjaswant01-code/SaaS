from django.db import models

# Create your models here.
class pagevisits(models.Model):
    #db - table
    #Id -> primary key -> autofield 1, 2, 3, 4, 5
    path = models.TextField(blank=True, null=True)  # colum
    timespan = models.DateField(auto_now_add=True) #colum