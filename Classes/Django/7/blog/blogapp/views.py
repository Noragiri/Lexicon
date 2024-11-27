from django.http import Http404
from django.shortcuts import get_object_or_404, render
from blogapp.models import Post

# Create your views here.


def index(request):
    return render(request, "blogapp/index.html")


def other(request):
    return render(request, "blogapp/other.html")


def homepage(request):
    post_list = Post.objects.all()
    context = {"post_list": post_list}

    return render(request, "blogapp/homepage.html", context)


def post(request, id):
    # Get the post with the given id, or return a 404 if it doesn't exist
    post = get_object_or_404(Post, id=id)

    return render(request, "blogapp/post_detail.html", {"post": post})


def relative(request):
    return render(request, "blogapp/relative_url_templates.html")
