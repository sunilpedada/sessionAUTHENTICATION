from django.conf.urls import url
from addcart.views import add,display
urlpatterns=[
    url(r"^toadd/$",add),
    url(r"^toadd/todisplay/$",display)
]