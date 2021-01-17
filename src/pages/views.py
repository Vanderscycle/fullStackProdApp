from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args, **kwargs):

    return render(request,'home.html',{})

def about_view(request,*args, **kwargs):
    context = {
        'author':'Henri Vandersleyen',
        'email':'hvandersleyen@gmail.com'
    }
    return render(request,'about.html',context)