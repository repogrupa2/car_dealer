from django.urls import path, include, reverse_lazy
import accounts.views as views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("register", views.register, name="register"),
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("home", views.home, name="home"),
    path('reset/', include('django.contrib.auth.urls')),
    path("password_reset/", auth_views.PasswordResetView.as_view(

        success_url=reverse_lazy("password_reset_done"),
        template_name="remind_password/password_reset_form.html",
        email_template_name="remind_password/password_reset_email.html",
    ), name="password_reset"),

    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="remind_password/password_reset_done.html"
        ),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="remind_password/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="remind_password/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
