from django.conf.urls import url
from rest.app.user.views import UserRegistrationView


urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    ]