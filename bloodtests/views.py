"""Module to define DRF view classes."""

from rest_framework import mixins, viewsets, status

from bloodtests.models import Test
from bloodtests.serializers import TestSerializer


class TestDetails(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """View class for Test model.

    The GenericViewSet class inherits from GenericAPIView, and provides the default set of get_object,
    get_queryset methods and other generic view base behavior, but does not include any actions by default.
    Ref: https://www.django-rest-framework.org/api-guide/viewsets/#genericviewset

    So we make use of the mixin classes to provide retrieve, create and update actions.
    We can then explicitly binding the allowed http methods to the appropriate actions in urls.py: urlpatterns.
    Ref: https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-mixins
    """
    serializer_class = TestSerializer
    lookup_field = "code"
    queryset = Test.objects.all()

    def create_or_update(self, request, *args, **kwargs):
        """Create or update Test record based on the code from url path exists or not.

        If code exists, call mixin update() method, otherwise call mixin create() method.
        """
        # If my understanding is correct, according to the test case test_post_basic() in test_bloodtests.py,
        # the http post method is expected to be responsible for both create and update of Test objects.
        # That means, performing update if code exists, otherwise create.
        if Test.objects.filter(pk=kwargs.get("code", "")).exists():
            res = super().update(request, *args, **kwargs)
        else:
            res = super().create(request, *args, **kwargs)

        # Besides, it is expected to return 200 as the successful status for both update and create.
        # So we will always return 200 if status is 200 or 201.
        if res.status_code in [status.HTTP_200_OK, status.HTTP_201_CREATED]:
            res.status_code = status.HTTP_200_OK

        return res
