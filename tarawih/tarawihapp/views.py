from django.http import FileResponse, Http404
from django.shortcuts import render
from django.conf import settings
from .models import *

# Create your views here.
def home(request):
    Nights = TarawihNight.objects.all()
    context = {"nights": Nights}
    return render(request, "home.html",{"nights": Nights})

#download view:
from pathlib import Path

def download_pdf(request):
    pdf_path = Path(settings.MEDIA_ROOT) / "tarwih_file.pdf"
    if not pdf_path.exists():
        raise Http404("PDF not found")

    return FileResponse(open(pdf_path, "rb"), as_attachment=True, filename="tarawih_nights.pdf")