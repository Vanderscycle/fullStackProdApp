from django.shortcuts import (
        render,
        get_object_or_404,
        redirect
    )

# Create your views here.

def journaling_view(request):
    context = {
        'object':obj
    }
    return render(request,'journaling/journal.html', context)