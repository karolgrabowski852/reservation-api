from django.urls import path
from .api import ListUsers, GetUserProfile, DeleteUser, CreateUser

urlpatterns = [
    path('', ListUsers.as_view(), name='user-list'),
    path('profile/', GetUserProfile.as_view(), name='user-profile'),
    path('delete/', DeleteUser.as_view(), name='user-delete'),
    path('create/', CreateUser.as_view(), name='user-create'),
]
