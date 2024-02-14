"""Module to define DRF serializers."""

from rest_framework import serializers

from bloodtests.models import Test
from bloodtests.exceptions import LowerAndUpperValueError


class TestSerializer(serializers.ModelSerializer):
    """Serializer class of Test model.

    Serializer class replicates a lot of information that's also contained in the model,
    so we use ModelSerializer class to simplify and keep the code DRY.
    """

    class Meta:
        model = Test
        fields = ("code", "name", "unit", "lower", "upper", "ideal_range",)

    def validate(self, data):
        """Validate object level data.

        To do any other validation that requires access to multiple fields,
        add a method called .validate() to Serializer subclass.
        This method takes a single argument, which is a dictionary of field values.
        Ref: https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
        """
        _lower = data.get("lower", None)
        _upper = data.get("upper", None)

        if _lower is None and _upper is None:
            raise LowerAndUpperValueError("Lower and upper cannot both be null.")

        if _lower and _upper:
            if _lower > _upper:
                raise LowerAndUpperValueError("Lower value can't exceed upper value.")

        return data
