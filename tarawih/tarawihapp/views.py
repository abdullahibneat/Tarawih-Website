from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    Nights = TarawihNight.objects.all()
    context = {"nights": Nights}
    return render(request, "home.html",{"nights": Nights})