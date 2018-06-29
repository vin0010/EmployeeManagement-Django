from datetime import datetime
from time import timezone

from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=60)
    age = models.SmallIntegerField
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    address = models.TextField
    id = models.AutoField
    std = models.SmallIntegerField
    remarks = models.TextField

    def __str__(self):
        return self.title
