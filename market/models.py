from django.db import models


class Farmer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Crop(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    quality = models.CharField(max_length=50)
    harvest_date = models.DateField()
    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class MarketPrice(models.Model):
    crop_name = models.CharField(max_length=100)
    market_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price_per_kg = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.crop_name} - {self.market_name}"