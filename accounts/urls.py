from . import views
from django.urls import path

urlpatterns = [
    path("token/", views.CookieTokenObtainPairView.as_view()),
    path("token/refresh/", views.CookieTokenRefreshView.as_view()),
    path("register/", views.ListAndRegisterView.as_view()),
    path("check-username/", views.check_username),
    path("me/", views.get_current_user),
]
