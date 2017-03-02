from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

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
        return Response(LinkedBookmarkResourceContext, status=status.HTTP_200_OK)

class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinkedBookmarkResource.objects.all()
    serializer_class = ResourceSerializer

    def get(self, request, *args, **kwargs):
        response = super(ResourceDetail, self).get(request, *args, **kwargs)
        response = addContextInHeader(reverse('linked-bookmark-app:resource-context', request=request), response)
        return response

    def options(self, request, *args, **kwargs):
        return Response(LinkedBookmarkResourceContext, status=status.HTTP_200_OK)

class ResourceContext(APIView):

    def get(self, request, *args, **kwargs):
        return Response(LinkedBookmarkResourceContext, status=status.HTTP_200_OK)

class ResourceItemList(generics.ListCreateAPIView):
    queryset = LinkedBookmarkItemResource.objects.all()
    serializer_class = ResourceItemSerializer

    def get_queryset(self):
        resource_id = self.kwargs.get('resource_id')
        if resource_id is not None:
            return self.queryset.filter(linkedBookmark=resource_id)
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        response = super(ResourceItemList, self).get(request, *args, **kwargs)
        response = addContextInHeader(reverse('linked-bookmark-app:resource-item-context', request=request), response)
        return response

    def options(self, request, *args, **kwargs):
        return Response(LinkedBookmarkItemResourceContext, status=status.HTTP_200_OK)

class ResourceItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinkedBookmarkItemResource.objects.all()
    serializer_class = ResourceItemSerializer

    def get_queryset(self):
        resource_id = self.kwargs.get('resource_id')
        if resource_id is not None:
            return self.queryset.filter(linkedBookmark=resource_id)
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        response = super(ResourceItemDetail, self).get(request, *args, **kwargs)
        response = addContextInHeader(reverse('linked-bookmark-app:resource-item-context', request=request), response)
        return response

    def options(self, request, *args, **kwargs):
        return Response(LinkedBookmarkItemResourceContext, status=status.HTTP_200_OK)


class ResourceItemContext(APIView):

    def get(self, request, *args, **kwargs):
        return Response(LinkedBookmarkItemResourceContext, status=status.HTTP_200_OK)

