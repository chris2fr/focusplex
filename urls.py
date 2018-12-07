from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('who/<int:who_id>',views.who, name='who'),
    path('what/<int:what_id>',views.what, name='what'),
]