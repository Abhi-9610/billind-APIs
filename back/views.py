from rest_framework import generics, authentication
from django.http import JsonResponse

from .models import *
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from .serializers import *
from rest_framework import generics, permissions

from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import authenticate
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
class EmployeeSignInView(ObtainAuthToken):

    permission_classes = [AllowAny]


    def post(self, request, *args, **kwargs):

        username = request.data.get('username', '')

        password = request.data.get('password', '')


        try:

            use = Employee.objects.get(username=username)

        except Employee.DoesNotExist:

            return Response({'message': 'User not found.', 'status': False}, status=HTTP_404_NOT_FOUND)


        user = authenticate(request, username=username, password=password)

        if use is None:

            return Response({'message': 'Invalid credentials.', 'status': False}, status=HTTP_401_UNAUTHORIZED)


        token, created = Token.objects.get_or_create(use=user)

        return Response({

            'token': str(token),

            'message': 'Successfully signed in!',

            'data': EmployeeSerializer(use).data

        })
class EmployeeList(generics.ListCreateAPIView):
    authentication_classes = [authentication.BasicAuthentication]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.BasicAuthentication]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ProductList(generics.ListCreateAPIView):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

class CustomerList(generics.ListCreateAPIView):

    queryset = Customer.objects.all()

    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Customer.objects.all()

    serializer_class = CustomerSerializer

class BillCustomer(generics.CreateAPIView):

    queryset = Invoice.objects.all()

    serializer_class = BillSerializer


    def perform_create(self, serializer):

        customer = Customer.objects.get(pk=self.kwargs['customer_pk'])

        serializer.save(customer=customer)

