from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

WATERS = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('E', 'Evening')
)

class Plant(models.Model):
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  care = models.TextField(max_length=250)

  def watered_for_today(self):
    return self.watering_set.filter(date=date.today()).count() >= len(WATERS)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'plant_id': self.id})

class Watering(models.Model):
  date = models.DateField('Watering Date')
  water = models.CharField(
    max_length=1,
    choices=WATERS,
    default=WATERS[0][0]
  )

  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

  def __str__(self):
      return f"{self.get_water_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

