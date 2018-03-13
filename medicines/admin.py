from django.contrib import admin
from . models import Products, Specification, Medicine
# Register your models here.

admin.site.register([Products, Specification, Medicine])
