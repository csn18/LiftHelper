from django.urls import path
from Main.views import main

urlpatterns = [
    path('', main, name='main')
]
