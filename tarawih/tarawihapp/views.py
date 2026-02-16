from django.http import FileResponse, Http404
from django.shortcuts import render
from django.conf import settings
from pathlib import Path

from .models import TarawihNight


# Create your views here.
def home(request):
    Nights = TarawihNight.objects.all()
    return render(request, "home.html", {"nights": Nights})


def rakah(request):
    # Prefetch related rakahs to avoid N+1 queries
    Nights = TarawihNight.objects.prefetch_related("rakahs").all()
    return render(request, "rakah.html", {"nights": Nights})


# download view:
def download_pdf(request):
    pdf_path = Path(settings.MEDIA_ROOT) / "Tarweeh 29 Nights, V4.pdf"
    if not pdf_path.exists():
        raise Http404("PDF not found")

    return FileResponse(open(pdf_path, "rb"), as_attachment=True, filename="tarawih_nights.pdf")