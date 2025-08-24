from django.db import models

# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name
    

class Supplier(models.Model) :
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, blank= True)


    def __str__(self) :
        return self.name
    

class Product(models.Model) :
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_on = models.DateTimeField(auto_now_add=True)


    def __self__(self):
        return self.name
    

