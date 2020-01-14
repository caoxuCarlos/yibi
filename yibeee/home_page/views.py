from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'home_page/home.html')