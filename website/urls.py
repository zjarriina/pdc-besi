from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('applications.html', views.applications, name="applications"),
    path('searchbar.html' , views.searchbar, name="searchbar"),
    path('post.html', views.post, name="post"),

]
