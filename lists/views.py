from django.shortcuts import render
from django.http import HttpRequest



# Create your views here.
def home_page(request):
   return render(request, 'home.html')

