"""Module to define exception classes and functions."""

from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


class LowerAndUpperValueError(APIException):
    """Custom exception for lower and upper validation errors."""

    def __init__(self, detail: str, code: int = status.HTTP_400_BAD_REQUEST):
        """
        Args:
             detail: Validation error message.
             code: Response status code, default is 400.
        """
        super().__init__(detail, code)
        self.detail = detail
        self.code = code


def base_exception_handler(exc, context):
    """Override DRF custom exception handler method in order to control the response message format.

    This is mainly for the test cases of object level validation (e.g. validate both lower and upper).
    As the default message format of serializers.ValidationError is {"non_field_errors": ["...error msg..."]},
    which will fail the test cases.
    So we make use of custom exception and exception_handler to control the error message format.

    IMPORTANT: This custom handler must be specified in settings.REST_FRAMEWORK["EXCEPTION_HANDLER"].

    Ref:
    https://www.django-rest-framework.org/api-guide/serializers/#validation
    https://medium.com/turkcell/request-validation-and-custom-exception-handling-in-django-rest-framework-649fddecb415
    """
    # Call DRF's default exception handler first to get the standard error response.
    response = exception_handler(exc, context)

    # If LowerAndUpperValueError is raised for lower and upper validation error,
    # then override the error message of the response.
    if type(exc) == LowerAndUpperValueError:
        response.status_code = exc.code
        response.data = exc.detail

    return response
