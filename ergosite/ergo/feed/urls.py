from django.urls import path
from . import views

urlpatterns = [
    path('ergo/', views.ergo, name='ergo'),
]
