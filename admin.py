from django.contrib import admin
from .models import Who, What # Base models we are administrating
from django.shortcuts import redirect # For redirecting to main website on changes

# Register your models here.

class WhatAdmin(admin.ModelAdmin):
    fields = ['action', 'result','with_who','public']
    list_display = ('action', 'result','with_who','public')
    
    def save_model(self, request, instance, form, change):
        instance.owner = request.user

        if not change or not instance.created_by:
            instance.created_by = request.user
        instance.modified_by = request.user
        instance.save()
        form.save_m2m()
        return instance
        
    def response_add(self, request, obj, post_url_continue=None):
        """Redirect to root on add"""
        return redirect('/')

    def response_change(self, request, obj):
        """Redirect to root on change"""
        return redirect('/')

    def response_delete(self, request, obj, post_url_continue=None):
        """Redirect to root on delete"""
        return redirect('/')

admin.site.register(Who)
admin.site.register(What, WhatAdmin)

