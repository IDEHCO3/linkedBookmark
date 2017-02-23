from rest_framework import generics
from linkedBookmarkApp.models import LinkedBookmarkResource, LinkedBookmarkItemResource
from serializers import ResourceSerializer, ResourceItemSerializer
# Create your views here.

class ResourceList(generics.ListCreateAPIView):
    queryset = LinkedBookmarkResource.objects.all()
    serializer_class = ResourceSerializer

class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinkedBookmarkResource.objects.all()
    serializer_class = ResourceSerializer


class ResourceItemList(generics.ListCreateAPIView):
    queryset = LinkedBookmarkItemResource.objects.all()
    serializer_class = ResourceItemSerializer

class ResourceItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinkedBookmarkItemResource.objects.all()
    serializer_class = ResourceItemSerializer

