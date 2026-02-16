# app/models.py
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class TarawihNight(models.Model):
    night_number = models.PositiveSmallIntegerField(
        unique=True,
        validators=[MinValueValidator(1), MaxValueValidator(29)],
    )

    start_surah = models.TextField(blank=True)  # can be a single surah number or a range like "2-3"
    start_ayah = models.TextField(blank=True)

    end_surah = models.TextField(blank=True)  # can be a single surah number or a range like "2-3"
    end_ayah = models.TextField(blank=True)

    class Meta:
        ordering = ["night_number"]

    def __str__(self):
        return f"Night {self.night_number}"


class TarawihRakah(models.Model):
    night = models.ForeignKey(
        TarawihNight,
        related_name="rakahs",
        on_delete=models.CASCADE,
    )

    rakah_number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])

    start_surah = models.TextField(blank=True)  # can be a single surah number or a range like "2-3"
    start_ayah = models.TextField(blank=True)

    end_surah = models.TextField(blank=True)  # can be a single surah number or a range like "2-3"
    end_ayah = models.TextField(blank=True)
    
    full_recitation = models.TextField(blank=True,)  # can be a list of surah:ayah pairs or a description of the full recitation for this rakah

    class Meta:
        ordering = ["night__night_number", "rakah_number"]
        constraints = [
            models.UniqueConstraint(fields=["night", "rakah_number"], name="uniq_rakah_per_night"),
        ]

    def __str__(self):
        return f"{self.night} – Rakah {self.rakah_number}"
