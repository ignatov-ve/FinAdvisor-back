from rest_framework import generics

from .models import Okved
from .serializers import OkvedSerializer


# Create your views here.
class OkvedListCreate(generics.ListCreateAPIView):
    queryset = Okved.objects.all()
    serializer_class = OkvedSerializer
