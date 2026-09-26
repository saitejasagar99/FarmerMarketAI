from django.contrib import admin
from .models import Farmer, Crop, MarketPrice

admin.site.register(Farmer)
admin.site.register(Crop)
admin.site.register(MarketPrice)