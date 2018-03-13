from django.db import models


# Create your models here.
class Products(models.Model):
    product_type = models.CharField(max_length=250)
    product_logo = models.CharField(max_length=1000)
    product_description = models.CharField(max_length=10000)

    def __str__(self):
        return self.product_type + ' - ' + self.product_description


class Medicine(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    med_name = models.CharField(max_length=250)
    med_description = models.CharField(max_length=10000)
    med_price = models.CharField(max_length=250)
    med_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.med_name + ' - ' + self.med_description


class Specification(models.Model):
    specification = models.ForeignKey(Medicine)
    manufacturer = models.CharField(max_length=250)
    salts = models.CharField(max_length=250)
    salts_quantity = models.CharField(max_length=100)

    def __str__(self):
        return self.salts
