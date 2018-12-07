from django.contrib import admin
from .models import Who, What

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

admin.site.register(Who)
admin.site.register(What, WhatAdmin)

