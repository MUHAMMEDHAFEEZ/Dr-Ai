from django.urls import path , include
from .views import register_user, user_login, user_logout
from .views import change_password

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]