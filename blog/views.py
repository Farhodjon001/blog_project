from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog_list_view(request):
    blogs=Blog.objects.all()

    context={
        'blogs':blogs,
    }
    return render(request, 'home.html',context=context)