from django.db import models

from user.models import User


class Category(models.Model):
    Name=models.CharField(max_length=120)

    def _str_(self):
        return self.Name

class SubCategory(models.Model):
    Category=models.ForeignKey(Category,related_name="categories",on_delete=models.CASCADE)
    Name=models.CharField(max_length=120)

    def _str_(self):
        return self.Name
          
class Product(models.Model):
    P_Id= models.CharField(max_length=1200)
    Name = models.CharField(max_length=1200)
    Description = models.CharField(max_length=12000)
    Category = models.ForeignKey(SubCategory,related_name="category",on_delete=models.CASCADE)
    Date = models.CharField(max_length=200)
    img = models.ImageField(upload_to='product_images')
    Phone = models.CharField(max_length=1200)
    User =  models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)


    def _str_(self):
        return self.P_Id    



