from django.shortcuts import (
        render,
        get_object_or_404,
        redirect
    )
# usefull to query db
from .models import (
        GratefulFor,
        SmallVictory
    )
# form to enter in db
from .forms import (
    GratefulForForm,
    SmallVictoryForm
    )

def journaling_list_view(request):
    # will need some logic to only allow per user
    querysetGrateful = GratefulFor.objects.all()
    querysetSmallVic = SmallVictory.objects.all()
    context = {
        "gratefulList":querysetGrateful,
        'smallVicList':querysetSmallVic
    }
    return render(request,'journaling/journal_list.html',context)

def journaling_create_view(request):

    # formGrateful = GratefulForForm(request.POST or None)
    formSmallVictory = SmallVictoryForm(request.POST or None)
    if formSmallVictory.is_valid():
        formSmallVictory.save()
        #clears all the fields after the post method
        formSmallVictory = SmallVictoryForm()

    # elif formGrateful.is_valid():
    #     formGrateful.save()
    #     #clears all the fields after the post method
    #     formGrateful = GratefulForForm()

    context = {
        # 'GratefulForm':formGrateful,
        'SmallVictoryForm':formSmallVictory 
    }
    return render(request,'journaling/journal_create.html',context)

def journaling_view(request):
    context = {
        'object':obj
    }
    return render(request,'journaling/journal.html', context)