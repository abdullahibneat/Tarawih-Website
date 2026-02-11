# app/models.py
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class TarawihNight(models.Model):
    night_number = models.PositiveSmallIntegerField(
        unique=True,
        validators=[MinValueValidator(1), MaxValueValidator(29)],
    )

    start_surah = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(114)])
    start_ayah = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    end_surah = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(114)])
    end_ayah = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    title = models.CharField(max_length=120, blank=True)  # optional, e.g. "Night 1"

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

    start_surah = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(114)])
    start_ayah = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    end_surah = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(114)])
    end_ayah = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        ordering = ["night__night_number", "rakah_number"]
        constraints = [
            models.UniqueConstraint(fields=["night", "rakah_number"], name="uniq_rakah_per_night"),
        ]

    def __str__(self):
        return f"{self.night} – Rakah {self.rakah_number}"
