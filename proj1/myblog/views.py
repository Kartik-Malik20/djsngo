from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'myblog/home.html')
    #return HttpResponse("home")
def contact(request):
    return render(request,'myblog/contact.html')
    #return HttpResponse("contact")

