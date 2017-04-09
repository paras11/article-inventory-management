from django.db import models

# Create your models here.
class ProductPost(models.Model):
    product_id =models.CharField(max_length=250)
    product_price = models.CharField(max_length=250)
    product_name=models.CharField(max_length=250)
    type_choices=(
        ('TV','TV'),
        ('AC','AC'),
    )
    product_type = models.CharField(max_length=20,choices=type_choices,default='TV')
    #product_image = models.CharField(max_length=250)
    product_image = models.FileField()
    product_quanty=models.CharField(max_length=250)

    def __str__(self):
        return self.product_name
