from django.urls import path
from .views import *
app_nam="catalog"
urlpatterns=[path("",HomeView.as_view(),name="home"),
             path("about/",AboutView.as_view(),name="about"),
             path("contact/",ContactView.as_view(),name="contact")

             ]