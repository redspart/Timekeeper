from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class TimeEntry(models.Model):
    # user = ?
    # project_code = ?
    # period
    description = models.TextField(max_length=150, blank=True, null=True)
    date = models.DateField()
    hours = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1), MaxValueValidator(24)])