from django.db import models

# Create your models here.


class ShippingCountry(models.Model):
    country = models.CharField(max_length=150)
    available = models.BooleanField(default=True)
    price = models.FloatField(default=0.0)

    class Meta:
        ordering = ('country',)
        verbose_name = "ShippingCountry"
        verbose_name_plural = "ShippingCountries"

    def __str__(self):
        return self.country


# class ShippingStation(models.Model):
#     country = models.ForeignKey(ShippingCountry, on_delete=models.CASCADE)
#     station = models.CharField(max_length=150)
#     price = models.FloatField(default=0.0)
#
#     class Meta:
#         ordering = ('country',)
#         verbose_name = "ShippingStation"
#         verbose_name_plural = "ShippingStations"

    # def __str__(self):
    #     return self.station
