from django.db import models

# Create your models here.
class bookShop(models.Model):
    name=models.CharField(max_length=20)
    img=models.ImageField(upload_to='pics',default='hhhh.png')
    desc=models.TextField()
    price=models.IntegerField()