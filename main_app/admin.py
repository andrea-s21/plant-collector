from django.contrib import admin
from .models import Plant
from .models import Watering

# Register your models here.

admin.site.register(Plant)
admin.site.register(Watering)
