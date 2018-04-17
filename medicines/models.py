from django.db import models


class Products(models.Model):
    product_type = models.CharField(max_length=250, primary_key=True)
    product_logo = models.FileField()
    product_description = models.CharField(max_length=10000)


class Medicine(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    med_name = models.CharField(max_length=250, primary_key=True)
    med_description = models.CharField(max_length=10000)
    med_price = models.CharField(max_length=250)
    med_logo = models.FileField()
    manufacturer = models.CharField(max_length=250)


class Specification(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    salt = models.CharField(max_length=100)
    salt_quantity = models.CharField(max_length=10)







