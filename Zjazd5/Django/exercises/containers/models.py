from django.db import models

# Create your models here.

CONTAINER_TYPES = (
    ('glassbottle', 'Glass Bottle'),
    ('plasticbottle', 'Plastic Bottle'),
    ('box', 'Box'),
)

class Container(models.Model):
    type = models.CharField(choices=CONTAINER_TYPES, max_length=50  )