from django import forms
from .models import What

class WhatForm(forms.Form):
    result = forms.ChoiceField(label='to',
        required=False,
        # choices=(('',' ')),
        )
    action = forms.CharField(label="do",
        max_length=255,
        required=True,
        )
    # id = forms.HiddenField()
    
    def __init__(self, *args, **kwargs):
        super(WhatForm, self).__init__(*args, **kwargs)
        self.fields['action'].widget.attrs.update({
            'autofocus': 'autofocus',
            'size':32
        })
        # self.fields['result'].choices.append(('',' '))
    
    #def __init__ (self, request):
    #    if request.user.is_authenticated:
    #        result = forms.ModelChoiceField(queryset=What.objects.order_by('result__id').filter(created_by=request.user))
    #    super(forms.Form, self).__init__(request)