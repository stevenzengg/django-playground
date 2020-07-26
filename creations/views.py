from django.shortcuts import render
from .models import Creation
# Create your views here.
def homepage(request):
    creations = Creation.objects
    return render(request, 'creations/home.html',{'creations':creations})
