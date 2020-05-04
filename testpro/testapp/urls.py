from django.conf.urls import url
from testapp.views import count_cookies
urlpatterns=[
    url(r"^count/$",count_cookies.as_view()),
]