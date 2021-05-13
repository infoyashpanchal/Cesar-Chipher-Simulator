from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
    #path('decrypt/', decrypt),
    #path('encrypt/', encrypt),
]
