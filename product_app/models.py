from django.db import models

# Create your models here.

class Product(models.Model):
    prd_no = models.CharField(primary_key=True, max_length=10)
    prd_name = models.CharField(max_length=20, blank=True, null=True)
    prd_price = models.IntegerField(blank=True, null=True)
    prd_maker = models.CharField(max_length=30, blank=True, null=True)
    prd_color = models.CharField(max_length=10, blank=True, null=True)
    ctg_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'