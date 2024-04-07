from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [

    path('employees/', EmployeeList.as_view(), name='employee-list'),

    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),

    path('products/', ProductList.as_view(), name='product-list'),

    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),

    path('customers/', CustomerList.as_view(), name='customer-list'),

    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),

    path('bill-customer/<int:customer_pk>/', BillCustomer.as_view(), name='bill-customer'),
    path('signin/', EmployeeSignInView.as_view(), name='signin'),
    # path('signup/', EmployeeSignUpView.as_view(), name='signin'),
    # path('analytics/', ProductSalesView.as_view(), name='analytics'),

]