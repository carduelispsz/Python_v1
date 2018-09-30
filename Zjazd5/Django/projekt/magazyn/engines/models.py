from django.db import models

# Create your models here.
RODZAJE_SILNIKA = (
    ("benzyna", "benzyna"),
    ("diesel", "diesel"),
    ("elektryk", "elektryk"),
)


class Engine(models.Model):
    pojemnosc = models.IntegerField(null=True, blank=True)
    ilosc_cylindrow = models.IntegerField(null=True, blank=True)
    #paliwo = models.CharField(max_length=50)
    rodzaj = models.CharField(choices=RODZAJE_SILNIKA, max_length=50, null=True, blank=True)

    # def __str__(self):
    #     return str(self.id) + " | " + self.pojemnosc