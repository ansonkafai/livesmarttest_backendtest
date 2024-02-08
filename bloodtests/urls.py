from django.urls import path
from .views import TestDetails

# Apart from inheriting the mixins in our view class,
# we also need to configure the allowed http methods in urlpatterns,
# by providing a binding of the allowed http methods and the corresponding action for each view.
# Ref: https://github.com/encode/django-rest-framework/blob/e7777cb1ee98c0215a5f1f082a88290eefa3e293/docs/tutorial/6-viewsets-and-routers.md
allowed_http_methods_binding = {
    "get": "retrieve",
    "post": "create_or_update"
}

urlpatterns = (
    path('test/<str:code>', TestDetails.as_view(allowed_http_methods_binding), name="test_details"),
)
