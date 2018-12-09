from django.shortcuts import get_object_or_404, render
from django.db.models import Q # for joining multiple queries
from .models import Who, What
from .forms import WhatForm

# Create your views here.

def index(request):
    whats = ()
    what_form = ""
    zoom_id = request.GET.get('zoom')
    if request.user.is_authenticated:
        whats = What.objects.order_by('result__id').filter(created_by=request.user)
        
        what_form = WhatForm()
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            # what_form = WhatForm(request.POST)
            # check whether it's valid:
            #if what_form.is_valid():
            # process the data in form.cleaned_data as required
            action = request.POST.get("action")
            what = What.objects.create(action=action,created_by=request.user)
            if request.POST.get("result"):
                result = What.objects.get(pk=request.POST.get("result"))
                what.result = result
            what.save()
        what_form.fields['result'].choices = (('','[Top]'),)
        for what in whats:
            what_form.fields['result'].choices.append((str(what.id),what.action))
            # form_whats = forms.ModelChoiceField(queryset=whats, empty_label=" ---- ")
        # ugliness below
        if request.method == 'POST':
            what_form.fields['result'].initial = request.POST.get("result")
            what_form.fields['result'].value = request.POST.get("result")
            
    else:
        query = Q(public=True)
        if(zoom_id):
            query = query & ( Q(id=zoom_id) | Q(result__id=zoom_id) )
        whats = What.objects.order_by('result__id').filter(query)
        
    if(zoom_id):
        whats = whats.filter(Q(result__id=zoom_id) |  Q(id=zoom_id) )
    
    return render(request, 'why/index.html', {'whats':whats,'what_form':what_form})

def who(request, who_id):
    return render(request, 'why/who.html', {})

def what(request, what_id):
    return render(request, 'why/what.html', {})