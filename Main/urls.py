from django.urls import path
from Main.views import main, login_user, registration_user

urlpatterns = [
    path('', main, name='main'),
    path('login/', login_user, name='login'),
    path('registration/', registration_user, name='register')
]
