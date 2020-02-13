from django.db import models


# Create your models here.

class Book(models.Model):
    """
    book继承了Model类
    """
    title = models.CharField(max_length=20)
    pub_date = models.DateField(default="1983-06-01")
    price = models.FloatField(max_length=100,default=100)

    def __str__(self):
        return self.title


class Hero(models.Model):
    """
    hero继承了Model
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=7, choices=(('male', '男'), ('female', '女')), default='male')
    content = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
