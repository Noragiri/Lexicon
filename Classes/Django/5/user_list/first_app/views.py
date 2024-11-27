from django.shortcuts import render
from .models import User

# Create your views here.


def index(request):
    return render(request, "index.html")


def users(request):
    users_list = User.objects.all()
    processed_records = []

    for user in users_list:
        processed_records.append(user.info())
    context = {"users_list": processed_records}
    return render(request, "users.html", context)
