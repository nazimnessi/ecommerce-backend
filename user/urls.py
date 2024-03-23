from django.urls import path

from user.views import IsUserLoginView, UserLoginView, UserLogoutView

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("isLogin/", IsUserLoginView.as_view(), name="isLogin"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
