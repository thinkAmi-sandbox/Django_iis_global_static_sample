from django.conf.urls import url
from .views import BlueIndexView

urlpatterns = [
    url(r'^$', BlueIndexView.as_view(), name='index'),
]