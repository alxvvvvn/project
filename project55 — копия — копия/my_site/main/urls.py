from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index ),
    path('page', views.page),
    path('page1', views.page1),
    path('page2', views.page2),
    path('page3', views.page3),
    path('page4', views.page4),
    path('page5', views.page5),
    path('page6', views.page6),
    path('page7', views.page7),
    path('page8', views.page8),
    path('page9', views.page9),
    path('page10', views.page10),
    path('page11', views.page11),
    path('page12', views.page12),
    path('page13', views.page13),
    path('page14', views.page14),
    path('page15', views.page15),
    path('results', views.results),
]
