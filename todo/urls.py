from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('heading/create/', views.heading_create, name='heading_create'),
    path('heading/<int:id>/', views.heading_detail, name='heading_detail'),
    path('heading/<int:id>/delete/', views.heading_delete, name='heading_delete'),


    path('todo/<int:heading_id>/create/',
         views.todo_create, name='todo_create'),
    path('todo/<int:id>/edit/', views.todo_edit, name='todo_edit'),
    path('todo/<int:id>/delete/', views.todo_delete, name='todo_delete'),
    path('todo/<int:id>/complete/', views.todo_complete, name='todo_complete'),

]
