"""Module to register models to Django admin."""

from django.contrib import admin
from .models import Test

admin.site.register(Test)
