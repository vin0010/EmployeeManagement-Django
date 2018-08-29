from django.conf.urls import url

from .views import (
                get_student,
                get_all_student,
                create_student,
                update_student,
                home_page
                )

urlpatterns = [
    url(r'(?P<id>\d+)/$', get_student, name="get_student"),
    url(r'all/$', get_all_student, name='all'),
    url(r'create/$', create_student),
    url(r'(?P<id>\d+)/edit/$', update_student, name="update"),
    url(r'', home_page, name="welcome")
]