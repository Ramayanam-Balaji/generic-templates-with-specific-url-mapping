from django.urls import path
app_name='anything'
from app11.views import ms
urlpatterns=[
    path('ms/',ms,name='ms')
]