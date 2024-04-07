from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomPasswordChangeForm, CustomPasswordResetForm, CustomPasswordResetConfirmForm

# app_name = 'account'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.logout, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('profile/<str:user_name>', views.profile, name='profile'),
    

    path('password-change/', auth_views.PasswordChangeView.as_view(
                            form_class=CustomPasswordChangeForm),
                            name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(),
                            name='password_change_done'),

    path("password_reset/", auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetForm),
         name="password_reset"),

    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),

    path("reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(form_class=CustomPasswordResetConfirmForm),
        name="password_reset_confirm",
    ),
    path("reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]


