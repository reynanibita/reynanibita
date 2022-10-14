from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"reynanibita/index.html")

def aboutme(request):
    return render(request,"reynanibita/aboutme.html")

def portpolio(request):
    return render(request,"reynanibita/portpolio.html")

def services(request):
    return render(request,"reynanibita/services.html")