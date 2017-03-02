from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from linkedBookmarkApp.models import LinkedBookmarkResource, LinkedBookmarkItemResource
from serializers import ResourceSerializer, ResourceItemSerializer
from context import *
# Create your views here.

class ResourceList(generics.ListCreateAPIView):
    queryset = LinkedBookmarkResource.objects.all()
    serializer_class = ResourceSerializer

    def get(self, request, *args, **kwargs):
        response = super(ResourceList, self).get(request, *args, **kwargs)
        response = addContextInHeader(reverse('linked-bookmark-app:resource-context', request=request), response)
        return response

    def options(self, request, *args, **kwargs):
        return Response(LinkedBookmarkResourceContext, status=200)

class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinkedBookmarkResource.objects.all()
    serializer_class = ResourceSerializer

    def get(self, request, *args, **kwargs):
        response = super(ResourceDetail, self).get(request, *args, **kwargs)
        response = addContextInHeader(reverse('linked-bookmark-app:resource-context', request=request), response)
        return response

    def options(self, request, *args, **kwargs):
        return Response(LinkedBookmarkResourceContext, status=200)

class ResourceContext(APIView):

    def get(self, request, *args, **kwargs):
        return Response(LinkedBookmarkResourceContext, status=200)

class ResourceItemList(generics.ListCreateAPIView):
    queryset = LinkedBookmarkItemResource.objects.all()
    serializer_class = ResourceItemSerializer

    def get(self, request, *args, **kwargs):
        response = super(ResourceItemList, self).get(request, *args, **kwargs)
        response = addContextInHeader(reverse('linked-bookmark-app:resource-item-context', request=request), response)
        return response

    def options(self, request, *args, **kwargs):
        return Response(LinkedBookmarkItemResourceContext, status=200)

class ResourceItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinkedBookmarkItemResource.objects.all()
    serializer_class = ResourceItemSerializer

    def get(self, request, *args, **kwargs):
        response = super(ResourceItemDetail, self).get(request, *args, **kwargs)
        response = addContextInHeader(reverse('linked-bookmark-app:resource-item-context', request=request), response)
        return response

    def options(self, request, *args, **kwargs):
        return Response(LinkedBookmarkItemResourceContext, status=200)


class ResourceItemContext(APIView):

    def get(self, request, *args, **kwargs):
        return Response(LinkedBookmarkItemResourceContext, status=200)

