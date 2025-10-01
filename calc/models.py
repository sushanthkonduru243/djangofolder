from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=300, null=True)
    age = models.CharField(max_length=300, null=True)
    date = models.DateTimeField(null=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=300, null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor')
    )
    name = models.CharField(max_length=300, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=300, choices=CATEGORY)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of Delivery', 'Out of Delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=300, choices=STATUS)
