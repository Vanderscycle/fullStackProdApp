from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args, **kwargs):

    return render(request,'home.html',{})
# we want to add a quick story
def about_view(request,*args, **kwargs):
    context = {
        'author':'Henri Vandersleyen',
        'github':'https://github.com/Vanderscycle'
    }
    return render(request,'about.html',context)

def contact_view(request,*args, **kwargs):
    """
    We want to set up the possibility to leave a message.
    We also want them to find a copy of my CV
    """
    context = {
        'email':'hvandersleyen@gmail.com'
        
    }
    return render(request,'contact.html',context)
