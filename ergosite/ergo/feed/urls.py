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
    path('dasn1u/', views.charname, {'player':'dasn1u'}, name='dasn1u'),
    path('dasn1u', views.charname, {'player':'dasn1u'}, name='dasn1u'),
    path('Dasn1u/', views.charname, {'player':'dasn1u'}, name='dasn1u'),
    path('Dasn1u', views.charname, {'player':'dasn1u'}, name='dasn1u'),
]
