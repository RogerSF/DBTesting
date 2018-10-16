from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^", views.index, name="index"),
    url(r"^login", views.login_view, name="login"),
    url(r"^signup", views.signup, name="signup"),
    url(r"^logout", views.logout_view, name="logout"),
    #url("portfolio", views.portfolio, name="portfolio"),
]