from django.conf.urls import url

from .views import (
                get_student,
                get_all_student
                )

urlpatterns = [
    url(r'(?P<id>\d+)/$', get_student, name="get_student"),
    url(r'all/$', get_all_student, name='all'),
]