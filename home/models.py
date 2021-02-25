from django.db import models

# # Create your models here.
class Categories(models.Model):
    categoryID = models.IntegerField()
    categoryName = models.CharField(max_length=50)
    categoryDescription = models.TextField()





