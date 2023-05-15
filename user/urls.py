from django.urls import path
from user import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/<pk>/', views.SingleUserPage, name='single-user'),
    path('user/remove_friend/<pk>/', views.remove_friend, name='remove-friend'),
    path('user/add_friend/<pk>/', views.add_friend, name='add-friend'),
]