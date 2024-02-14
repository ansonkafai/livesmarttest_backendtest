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

    @property
    def ideal_range(self):
        """Render the derived field 'ideal_range' based on lower and upper values.
        """
        if self.lower and self.upper:
            return f"{self.lower} <= value <= {self.upper}"
        elif self.lower is None and self.upper:
            return f"value <= {self.upper}"
        elif self.lower and self.upper is None:
            return f"value >= {self.lower}"
        else:
            return ""
