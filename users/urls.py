from rest_framework import routers
from django.urls import path
from users import views

router = routers.DefaultRouter()

urlpatterns = [
    path(r'register', views.UserRegistrationView.as_view()),
    path(r'login', views.UserLoginView.as_view())
]
