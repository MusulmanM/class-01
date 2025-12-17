from django.shortcuts import render
from .models import Post, Post_view, Post_comment
# Create your views here.



def home_page(request):
    context = {
        "posts": Post.objects.all().order_by("id")
    }

    return render(request, "index.html", context=context)