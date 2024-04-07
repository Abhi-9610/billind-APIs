from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()




class Product(models.Model):

    name = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    quantity = models.IntegerField()


    def __str__(self):

        return self.name


class Sale(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    employee = models.ForeignKey(User, on_delete=models.CASCADE)

    quantity = models.IntegerField()

    date = models.DateField(auto_now_add=True)


    def __str__(self):

        return f"{self.product.name} sold by {self.employee.username} on {self.date}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer.name}'s order for {self.quantity} {self.product.name}"

class Employee(models.Model):
    username = models.CharField(max_length=100)
    number=models.IntegerField()
    password=models.CharField(max_length=10)
    # Add other fields as needed


class Invoice(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True)

    total_amount = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):

        return f"Invoice {self.pk} for {self.customer.username}"