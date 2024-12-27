from django.urls import path
from . import views

urlpatterns=[
    path('reg',views.reg),
    path('',views.log),
    path('upload_file',views.upload_file),
    path('home',views.home),
    path('logout',views.logout)
    
]