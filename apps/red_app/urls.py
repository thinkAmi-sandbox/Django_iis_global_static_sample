from django.conf.urls import url
from .views import RedIndexView

urlpatterns = [
    url(r'^$', RedIndexView.as_view(), name='index'),
]