from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    #  path('send-mail/', views.send_mail_view, name='send_mail_view'),
    
]