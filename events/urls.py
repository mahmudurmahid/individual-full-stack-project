from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.event_list, name='event_list'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('my-events/', views.my_events, name='my_events'),
    path('create/', views.create_event, name='create_event'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book-event/<int:event_id>/', views.book_event, name='book_event'),
]
