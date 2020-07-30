from django.http import HttpResponse
from django.conf.urls import url
from django.urls import path
from first_app import views
urlpatterns=[

    path('',views.view2,name='extensionview')
]
# Create your views here.