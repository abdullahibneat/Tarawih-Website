# app/admin.py
from django.contrib import admin
from .models import TarawihNight, TarawihRakah

class TarawihRakahInline(admin.TabularInline):
    model = TarawihRakah
    extra = 0

@admin.register(TarawihNight)
class TarawihNightAdmin(admin.ModelAdmin):
    list_display = ("night_number", "start_surah", "start_ayah", "end_surah", "end_ayah")
    inlines = [TarawihRakahInline]
