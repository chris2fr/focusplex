from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('read/<int:id>', views.read, name='read'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('read/<int:id>', views.read, name='read'),
    path('read/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('who/<int:who_id>',views.who, name='who'),
    path('what/<int:what_id>',views.what, name='what'),
]