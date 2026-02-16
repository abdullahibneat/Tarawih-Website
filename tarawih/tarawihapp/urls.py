from django.urls import path
from tarawihapp import views

urlpatterns = [
    path("",views.home, name='home'),
    path("rakah/<int:night_number>/", views.rakah, name='rakah'),
    path("download/", views.download_pdf, name="download_pdf"),
]