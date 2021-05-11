from django.conf.urls import url
from users_profile.views import UserProfileView


urlpatterns = [
    url(r'profile', UserProfileView.as_view()),
]
