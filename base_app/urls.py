from django.urls import path

from . import views

urlpatterns = [
    # ex '/base_app/'
    path('', views.index, name='index'),
    #  ex '/base_app/<some_string>'
    path('translit/<str:some_string>/', views.translit_this, name='translit_this'),
    #  ex '/base_app/normal/<some_string>'
    path('normal/<str:some_string>/', views.normal_this, name='normal_this'),
]
