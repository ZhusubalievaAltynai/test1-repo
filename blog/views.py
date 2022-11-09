from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World')
def blog_all(request):
    post = models.Post.objects.all()
    return render(request, 'hello.html',{'post':post})