from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Django'
    dest1.percent = 40
    return render(request,'index.html',{'dest1': dest1})