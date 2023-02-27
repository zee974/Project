from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def about(request):
    return HttpResponse("This is ABout")

def contact(request):
    template = loader.get_template("contact.html")
    return HttpResponse(template.render())

def products(request):
    template =loader.get_template("products.html")
    return HttpResponse(template.render())

def faqs(request):
    template =loader.get_template("faqs.html")
    return HttpResponse(template.render())
def careers(request):
    template =loader.get_template("careers.html")
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())

def logindash(request):
    template = loader.get_template("logindash.html")
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template("signup.html")
    return HttpResponse(template.render())


