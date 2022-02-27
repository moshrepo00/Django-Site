from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:team_id>/detail/', views.team_detail, name='team_detail'),
    path('<int:team_id>/coaches/', views.coaches, name='coaches'),
]
