from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.test, name='main'),
    path("summarize/", views.makeSmr, name='smr'),
]
