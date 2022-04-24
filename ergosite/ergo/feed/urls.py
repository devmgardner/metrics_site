from django.urls import path
from . import views

urlpatterns = [
    path('ergo/', views.charname, {'player':'Ergo'}, name='ergo'),
    path('ergo', views.charname, {'player':'Ergo'}, name='ergo'),
    path('Ergo/', views.charname, {'player':'Ergo'}, name='ergo'),
    path('Ergo', views.charname, {'player':'Ergo'}, name='ergo'),
    path('alinthar/', views.charname, {'player':'Alinthar'}, name='alinthar'),
    path('alinthar', views.charname, {'player':'Alinthar'}, name='alinthar'),
    path('Alinthar/', views.charname, {'player':'Alinthar'}, name='alinthar'),
    path('Alinthar', views.charname, {'player':'Alinthar'}, name='alinthar'),
    path('naevyse/', views.charname, {'player':'Naevyse'}, name='naevyse'),
    path('naevyse', views.charname, {'player':'Naevyse'}, name='naevyse'),
    path('Naevyse/', views.charname, {'player':'Naevyse'}, name='naevyse'),
    path('Naevyse', views.charname, {'player':'Naevyse'}, name='naevyse'),
    path('Alrick35/', views.charname, {'player':'Alrick35'}, name='alrick35'),
    path('Alrick35', views.charname, {'player':'Alrick35'}, name='alrick35'),
    path('alrick35/', views.charname, {'player':'Alrick35'}, name='alrick35'),
    path('alrick35', views.charname, {'player':'Alrick35'}, name='alrick35'),
]
