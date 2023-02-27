from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [ 
    path("", views.index, name = 'index'),
    path("about", views.about, name = "about"),
    path("contact", views.contact, name = "contact"),
    path("signup", views.signup, name = "signup"),
    path("login", views.login, name = "login"),
    path("logindash", views.logindash, name = "logindash"),
    path("products", views.products, name = "products"),
    path("faqs", views.faqs, name = "faqs"),
    path("careers", views.careers, name = "careers"),
]