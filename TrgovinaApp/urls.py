# Django imports
from django.conf.urls import url
# Project imports
from . import views

urlpatterns = [
    url(r'^$', views.payment, name='payment'),
    url(r'new/', views.new, name='new'),
    url(r'history/', views.history, name='history'),
    url(r'all_cards/', views.all_cards, name='all_cards'),
    url(r'(?P<id>\d+)/$', views.card_delete, name='card_delete'),
]
