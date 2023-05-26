from django.urls import path
app_name='something'
from app12.views import virat
urlpatterns=[
    path('virat/',virat,name='virat')
]