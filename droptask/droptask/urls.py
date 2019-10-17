from django.contrib import admin
from django.urls import path, include
from todolist import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('task/', include('todolist.urls')),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
