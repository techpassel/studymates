from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Home page")
    return render(request, 'home.html')

def room(request):
    # return HttpResponse("Room page")
    return render(request, 'room.html')