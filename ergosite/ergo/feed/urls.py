from django.urls import path
from . import views

urlpatterns = [
    path('ergo/', views.charname('','Ergo'), name='ergo'),
    path('ergo', views.charname('','Ergo'), name='ergo'),
    path('Ergo/', views.charname('','Ergo'), name='ergo'),
    path('Ergo', views.charname('','Ergo'), name='ergo'),
    path('alinthar/', views.charname('','Alinthar'), name='alinthar'),
    path('alinthar', views.charname('','Alinthar'), name='alinthar'),
    path('Alinthar/', views.charname('','Alinthar'), name='alinthar'),
    path('Alinthar', views.charname('','Alinthar'), name='alinthar'),
    path('dasn1u/', views.charname('','dasn1u'), name='dasn1u'),
    path('dasn1u', views.charname('','dasn1u'), name='dasn1u'),
    path('Dasn1u/', views.charname('','dasn1u'), name='dasn1u'),
    path('Dasn1u', views.charname('','dasn1u'), name='dasn1u'),
]
