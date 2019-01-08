from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

#def get_sentinel_user():
#    return get_user_model().objects.get_or_create(username='I')[0]

class BaseModel(models.Model):
    """ Common attributes and methods to all models.
    """
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    app_name = 'taskphrase'
        
    class Meta:
        abstract = True
        
    def save_model(self, request, instance, form, change):
        """ Utility to add the current user to the current object.
        """
        user = request.user 
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
        instance.modified_by = user
        instance.save()
        form.save_m2m()
        return instance
        
class Who(BaseModel):
    """These are the contacts involved with the Whats.
    """
    name = models.CharField(max_length=255)
    do_does = models.CharField(max_length=16,default="do",
        choices=(('do','do'),('does','does')),)
    first_name = models.CharField(max_length=48,
        null=True,blank=True,)
    last_name = models.CharField(max_length=48,
        null=True,blank=True,)
    django_user_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='user_contact')
    notes = models.TextField(
        null=True,
        blank=True,
    )
    email = models.CharField(max_length=128,
        null=True,
        blank=True,)
    tel = models.CharField(max_length=128,
        null=True,
        blank=True,)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
class What(BaseModel):
    """A 'What' is also a 'Why' for other 'What's, the basis of the application.
    """
    action = models.CharField(max_length=255,)
    who = models.ForeignKey(Who,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,)
    result = models.ForeignKey('self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,)
    public = models.BooleanField(default=False)
    with_who = models.ForeignKey(Who,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='with_who',)
    for_whom = models.ForeignKey(Who,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='for_whom',)
    notes = models.TextField(blank=True,
        null=True,)
        
    def __str__(self):
        return self.action

    def __repr__(self):
        return self.action
