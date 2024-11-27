from django.urls import path
from blogapp import views

# TEMPLATE TAGGING

app_name = "blogapp"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("relative/", views.relative, name="relative"),
    path("other/", views.other, name="other"),
    path("post/<int:id>/", views.post, name="post"),
]
