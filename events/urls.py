from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),  # static homepage
    path('events/', views.event_list, name='event_list'),  # events page
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='events/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
