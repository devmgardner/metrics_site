from django.urls import path
from . import views

urlpatterns = [
    path('ergo/', views.ergo, name='ergo'),
    path('ergo', views.ergo, name='ergo'),
    path('Ergo/', views.ergo, name='ergo'),
    path('Ergo', views.ergo, name='ergo'),
    path('alinthar/', views.alinthar, name='alinthar'),
    path('alinthar', views.alinthar, name='alinthar'),
    path('Alinthar/', views.alinthar, name='alinthar'),
    path('Alinthar', views.alinthar, name='alinthar'),
    path('dasn1u/', views.dasn1u, name='dasn1u'),
    path('dasn1u', views.dasn1u, name='dasn1u'),
    path('Dasn1u/', views.dasn1u, name='dasn1u'),
    path('Dasn1u', views.dasn1u, name='dasn1u'),
]
