from django.urls import path
from basic_app import views
from django.contrib.auth.views import LogoutView

# TEMPLATES URLS

app_name = "basic_app"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.custom_logout_view, name="logout"),
]
