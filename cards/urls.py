from django.urls import path

from . import views

urlpatterns = [
    # ex '/cards/'
    path('', views.index, name='index'),
]
