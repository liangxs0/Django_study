from django.urls import path, re_path
from .views import UserAll, UserLogin, UserRegister, CreateDir, DirList, DirDetial
from django import views

app_name = 'blog'
urlpatterns = [
    path(r'users/', UserAll.as_view(), name='users'),
    path(r'users/register/', UserRegister.as_view(), name='user_register'),
    path(r'users/login/', UserLogin.as_view(), name='user_login'),
    path(r'dir/create/', CreateDir.as_view(), name='dir_create'),
    path(r'dir/<int:user_id>/', DirList.as_view(), name='dir_list'),
    path(r'dir/detial/', DirDetial.as_view(), name='dir_detial'),
]


