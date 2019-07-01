# Django imports
from django.conf.urls import url
# Project imports
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
