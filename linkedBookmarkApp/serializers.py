from rest_framework import serializers
from linkedBookmarkApp.models import LinkedBookmarkResource, LinkedBookmarkItemResource

class ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = LinkedBookmarkResource
        fields = ('id', 'name', 'description', 'user')

class ResourceItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = LinkedBookmarkItemResource
        fields = ('id', 'name', 'description', 'iri', 'linkedBookmark')
