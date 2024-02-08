"""Module to define Django model classes."""

from django.db import models


class Test(models.Model):
    """Model class represents the information of a Test.
    """
    code = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)
    lower = models.FloatField(null=True, blank=True)
    upper = models.FloatField(null=True, blank=True)
