# cyber/urls.py
from django.urls import path
from .views import (
    cyber_form_view, 
    cyber_result_view, 
    user_login, 
    user_signup, 
    user_logout
)

urlpatterns = [
    path('', cyber_form_view, name='cyber_form'),
    path('result/<int:log_id>/', cyber_result_view, name='cyber_result'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
]
