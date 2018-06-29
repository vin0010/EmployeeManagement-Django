from django.conf.urls import url

from .views import (
                get_student)

urlpatterns = [
    url(r'(?P<id>\d+)/$', get_student),
]