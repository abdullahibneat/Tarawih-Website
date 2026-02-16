# views.py
from django.http import FileResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from pathlib import Path

from .models import TarawihNight


def home(request):
    nights = TarawihNight.objects.all()
    return render(request, "home.html", {"nights": nights})


def rakah(request, night_number):
    night = get_object_or_404(
        TarawihNight.objects.prefetch_related("rakahs"),
        night_number=night_number
    )
    return render(request, "rakah_detail.html", {"night": night})


def download_pdf(request):
    pdf_path = Path(settings.MEDIA_ROOT) / "Tarweeh 29 Nights, V4.pdf"
    if not pdf_path.exists():
        raise Http404("PDF not found")

    return FileResponse(open(pdf_path, "rb"), as_attachment=True, filename="tarawih_nights.pdf")