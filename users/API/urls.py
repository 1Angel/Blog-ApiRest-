from users.API.views import registration_view, login
from django.urls import path
urlpatterns =[
    path('login/', login, name='login'),
    path('register/', registration_view, name='register')
]