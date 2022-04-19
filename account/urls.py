from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm, PasswordReForm, PasswordReConfirmForm 
from django.views.generic.base import TemplateView

app_name = 'account'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='account/registration/login.html',form_class=UserLoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/account/login/'),name='logout'),
    path('register/',views.account_register,name='register'),
    path('activate/<slug:uidb64>/<slug:token>/',views.account_activate,name='activate'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile/edit/',views.edit_details,name='edit_details'),
    path('profile/delete_user/',views.delete_user,name='delete_user'),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='account/user/password_reset.html',success_url = 'password_reset_email_confirm', email_template_name = 'account/user/password_reset_email_template.html', form_class=PasswordReForm),name='password_reset'),

    path('password_reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='account/user/password_reset_confirm.html',success_url='password_reset_complete/',form_class=PasswordReConfirmForm),name='password_reset_confirm'),

    path('profile/delete_confirm/',TemplateView.as_view(template_name='account/user/delete_confirm.html'),name='delete_confirmation'),

    path('password_reset/password_reset_email_confirm/',TemplateView.as_view(template_name='account/user/reset_password_info.html'),name='reset_password_info'),
    path('password_reset_confirm/Mg/password_reset_complete/',TemplateView.as_view(template_name="account/user/reset_password_info.html"), name='password_reset_complete')
]
