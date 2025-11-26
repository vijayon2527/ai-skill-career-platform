from django.urls import path
from .views import *

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),

    path("users/", UsersListView.as_view()),
    path("users/<int:user_id>/update/", UserUpdateView.as_view()),
    path("users/<int:user_id>/delete/", UserDeleteView.as_view()),
]
