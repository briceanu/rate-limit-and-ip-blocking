from .models import CarModel
from .serializers import CarModelSerializer
from rest_framework import generics
from rest_framework.throttling import AnonRateThrottle
from .permissions import Prevent_Country_IPs
from rest_framework.permissions import IsAuthenticated



class PostCarAPI(generics.ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    """
     allow only a specified number of requests 
     the number of requests that the client can make is sepcified in settings.py
    """
    throttle_classes = [AnonRateThrottle]
    permission_classes = [Prevent_Country_IPs,IsAuthenticated]



 