from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.handle_login, name='login'),
    path('logout/', views.handle_logout, name='logout'),
    path('access/', views.access, name='access'),
]
