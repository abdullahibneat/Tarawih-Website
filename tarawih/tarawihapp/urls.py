from django.urls import path
from tarawihapp import views

urlpatterns = [
    path("",views.home, name='home'),
    path("download/", views.download_pdf, name="download_pdf"),
]