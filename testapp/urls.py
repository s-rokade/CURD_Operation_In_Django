#from django.contrib import admin
from django.urls import path
#from django.urls.resolvers import URLPattern
from . import views
urlpatterns= [
    path('', views.add_retriew_data, name= 'homepage'),
    path('delete/<int:id>/', views.deletestudent, name='deletedata'),
    path('update/<int:id>/', views.update_data, name='updatedata'),
]