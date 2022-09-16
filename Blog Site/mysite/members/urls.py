from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


app_name='members'

urlpatterns = [
    
    path('register/',views.UserRegister.as_view(),name='register'),
    path('edit_profile/',views.UserEditProfile.as_view(),name='edit_profile'),   
    path('password/',views.PasswordChangeView.as_view(template_name='registration/password_change.html'),name='password_change'),
    path('pswrd_success/',views.password_success,name='pswrd_success'),
    path('<int:pk>/profile_page/',views.ShowProfilePage.as_view(),name='profile_page'),
    path('<int:pk>/edit_profile_page/',views.EditProfilePage.as_view(),name='edit_profile_page'),
    path('create_profile_page/',views.CreateProfilePage.as_view(),name='create_profile_page'),

]
