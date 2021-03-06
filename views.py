from django.shortcuts import get_object_or_404, render
from django.db.models import Q # for joining multiple queries
from .models import Who, What
from .forms import WhatForm
import django.forms.widgets
from django.contrib import auth
from django.forms import formset_factory

from django.shortcuts import redirect # For redirecting to main website on changes

# Create your views here.
def first_letter_downcase(s):
    if (s):
        return s[:1].lower() + s[1:]
    else: 
        return
        
def create(request):
    """Creates a new TaskWhy"""
    what = ''
    id_result = ''
    if (request.POST.get("result")):
        id_result = request.POST.get("result")
    # Handle POST Add first
    if request.user.is_authenticated and request.method == 'POST':
        # create a form instance and populate it with data from the request:
        what_form = WhatForm(request.POST)
        if (id_result):
            what = What.objects.get(pk=id_result)
            what_form.fields['result'].choices.append((what.id,what.action))
        # check whether it's valid:
        if what_form.is_valid():
        # process the data in form.cleaned_data as required
            what = What.objects.create(
                # action = first_letter_downcase(what_form.cleaned_data["action"]),
                action = what_form.cleaned_data["action"],
                created_by = request.user)
            id_result = what_form.cleaned_data["result"]
            if (id_result and int(id_result) > 0):
                what.result = What.objects.get(pk=id_result)
            what.save()
    if(not id_result):
        id_result = '0'
    return redirect('/read/{}'.format(id_result))
    
def generic_update(request, id):
    # Handle POST Add first
    what = ''
    id_result = 0
    if request.user.is_authenticated and request.method == 'POST':       
        # process the data in form.cleaned_data as required
        what_form = WhatForm(request.POST)
        id_result = 0
        if (request.POST.get("result")):
            id_result = request.POST.get("result")
            what_result = What.objects.get(pk=id_result)
            what_form.fields['result'].choices.append((what_result.id,what_result.action))
        if what_form.is_valid():
            what = What.objects.get(pk=id)
            if (request.POST.get("order")):
                order = request.POST.get("order")
            # what.action = first_letter_downcase(what_form.cleaned_data["action"])
            what.action = what_form.cleaned_data["action"]
            what.modified_by = request.user
            if(id_result):
                what.result = what_result # Check on this one
            else:
                what.result = None
            what.save()
            return what
        else:
            return None
    else:
        return None

def update(request, id):
    """Updates an existing TaskWhy"""
    what = generic_update(request, id)
    return redirect('/read/{}'.format(id))

def order(request, id):
    """Updates the order of a subtask"""

    # what = generic_update(request, id)
    what = What.objects.get(pk=id)
    if (request.POST.get("order")):
        order = request.POST.get("order")
        what.order = order
        what.save()
    if (what.result):
        return redirect('/read/{}'.format(what.result.id))
    else:
        return redirect('/read/0')

# @login_required
def delete(request, id):
    """Deletes an existing TaskWhy"""
    result__id = False
    # Handle POST Add first
    if request.user.is_authenticated:
        what = get_object_or_404(What, pk=id)
        if (what.result):
            result__id = what.result.id
        what.delete()
    if (result__id):
        return redirect('/read/{}'.format(result__id))
    else:
        return redirect('/')
    
def read(request, id):
    """Loads an existing TaskWhy"""
    what_ups = []
    what_downs = []
    what_now = ''
    what_tops = []
    what_up_sides = []
    what_now_form = WhatForm()
    what_new_form = WhatForm()
    zoom_id = id
    
    if request.user.is_authenticated:
        filter = Q(created_by=request.user)
    else:
        return redirect('/accounts/login')
        # filter = Q(public=True)
    
    if (not zoom_id or int(zoom_id) is 0):
        what_now = What.objects.order_by('order','action').filter(filter).filter(result__id=None).first()
        if(not what_now):
            what_now = What.objects.create(
                action = "be {}".format(request.user),
                created_by = request.user)
        zoom_id = what_now.id
    else:
        what_now = What.objects.order_by('order','action').filter(filter).get(pk=zoom_id)
            
    for what in What.objects.order_by('order','action').filter(filter).filter(result__id=None).all():
        what_tops.append(what)

    what_downs_formset = formset_factory(WhatForm)

    for what in What.objects.order_by('order','action').filter(filter).filter(result__id=zoom_id).all(): # Down
        what_downs.append(what) 
    # Now up
    what = What.objects.get(pk=zoom_id)
    while(what.result): # up
        what_ups.insert(0,What.objects.order_by('order','action').filter(filter).get(pk=what.result.id))
        what = what.result
    # New up sides
    what = What.objects.order_by('order','action').filter(filter).get(pk=zoom_id)
    if (what.result):
        for whati in What.objects.order_by('order','action').filter(filter).filter(result__id=what.result.id).all():
            what_up_sides.append(whati)
    else:
        what_up_sides = what_tops
            
    if request.user.is_authenticated:
        what_new_form.fields['result'].widget = django.forms.widgets.HiddenInput()
        what_now_form.fields['result'].choices = (())
        whats = []
        for what in what_ups:
            # what_new_form.fields['result'].choices.append((str(what.id),what.action))
            what_now_form.fields['result'].choices.append((str(what.id),what.action))
            whats.insert(0,what)
        if (what_now):
            # what_new_form.fields['result'].choices.append((str(what_now.id),what_now.action))
            whats.append(what_now)
        for what in what_downs:
            # what_new_form.fields['result'].choices.append((str(what.id),what.action))
            whats.append(what)

        for what in what_up_sides:
            if (what.id != id and what.result):
                what_now_form.fields['result'].choices.append((str(what.id),what.action))
            
        if (zoom_id and int(zoom_id) > 0): # Very silly repetition
            what_new_form.fields['result'].initial = zoom_id
            what_new_form.fields['result'].value = zoom_id
        else:
            what_new_form.fields['result'].initial = request.POST.get("result__id")
            what_new_form.fields['result'].value = request.POST.get("result__id")
            
        # what_now_form = what_new_form # I hope this is a copy
        if (what_now):
            what_now_form.fields['action'].value = what_now.action
            what_now_form.fields['action'].initial = what_now.action
            if(what_now.result):
                what_now_form.fields['result'].initial = what_now.result.id
                what_now_form.fields['result'].value = what_now.result.id
            else:
                what_now_form.fields['result'].initial = ''
                what_now_form.fields['result'].value = ''
            del(what_now_form.fields['action'].widget.attrs['autofocus'])
            what_now_form.fields['action'].widget.attrs['onChange'] = 'javascrip:this.form.submit();'

    if (not zoom_id):
        zoom_id = 0
    return render(request, 'why/read.html', {
        'what_tops':what_tops,
        'what_ups':what_ups,
        'what_downs':what_downs,
        'what_now':what_now,
        'what_up_sides':what_up_sides,
        'what_now_form':what_now_form,
        'what_new_form':what_new_form,
        'zoom_id':int(zoom_id),
        }
        )

def index(request):
    """Shows Top-Level TaskWhys"""
    return redirect('/read/0')

def login(request):
    if (request.method == 'POST'):
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    return redirect('/')
        #if user is not None:
            # A backend authenticated the credentials
        #else:
            # No backend authenticated the credentials
def logout(request):
    auth.logout(request)
    return redirect('/read/0')
    
def who(request, who_id):
    return render(request, 'why/who.html', {})

def what(request, what_id):
    return render(request, 'why/what.html', {})