from django.db import models

# Create your models here.
from engines.models import Engine

TYP_NADWOZIA = (
    ('hatchback', 'hatchbag'),
)


class Car(models.Model):
    marka = models.CharField(max_length=255)
    model = models.CharField(max_length=50)
    rok_prod = models.IntegerField()
    nadwozie = models.CharField(choices=TYP_NADWOZIA, max_length=50, blank=True, null=True)
    engine = models.ForeignKey(Engine, on_delete = models.DO_NOTHING)

    def __str__(self):
        return f"{self.marka} -- {self.model}"