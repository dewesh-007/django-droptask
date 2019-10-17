from todolist import views
from django.urls import path

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('login/', views.user_login, name='login')
]
