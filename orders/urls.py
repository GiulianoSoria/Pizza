from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup_view, name="signup"),
    path("login", views.login_view, name="login"),
    path("cart", views.cart_view, name="cart"),
    path("logout", views.logout_view, name="logout")
]
