from django import forms
from .models import What

class WhatForm(forms.Form):
    result = forms.ChoiceField(label='resulting action',
        required=False,
        # choices=(('',' ')),
        )
    action = forms.CharField(label="initiating action",
        max_length=255,
        required=True,
        help_text="verb phrase (or task however you wish to express it)",
        )
    order = forms.CharField(label="order",
        max_length = 12,
        required = False,
        help_text = "order of presentation",
        widget=forms.TextInput(attrs={'size':4}),
        )
    # id = forms.HiddenField()
    
    def __init__(self, *args, **kwargs):
        super(WhatForm, self).__init__(*args, **kwargs)
        self.fields['action'].widget.attrs.update({
            'autofocus': 'autofocus',
            'size':32,
            'placeholder':self.fields['action'].help_text
        })
        self.fields['order'].widget.attrs.update({
            'size':4,
            'placeholder':self.fields['order'].help_text
        })
        # self.fields['action'].widget.help_text = self.fields['action'].help_text
        self.fields['result'].widget.attrs.update({
            'onChange': 'javascrip:this.form.submit();',
        })
        # self.fields['result'].choices.append(('',' '))
    
    #def __init__ (self, request):
    #    if request.user.is_authenticated:
    #        result = forms.ModelChoiceField(queryset=What.objects.order_by('result__id').filter(created_by=request.user))
    #    super(forms.Form, self).__init__(request)
    
