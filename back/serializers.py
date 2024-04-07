from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class BillSerializer(serializers.ModelSerializer):

    class Meta:

        model = Invoice

        fields = ['id', 'customer', 'date', 'total_amount']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','quantity','price']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
class SaleSerializer(serializers.ModelSerializer):

    product = serializers.StringRelatedField()

    employee = serializers.StringRelatedField()


    class Meta:

        model = Sale

        fields = '__all__'