from rest_framework import serializers
from linkedBookmarkApp.models import LinkedBookmarkResource, LinkedBookmarkItemResource

class ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = LinkedBookmarkResource
        fields = ('name', 'description', 'user')

class ResourceItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = LinkedBookmarkItemResource
        fields = ('name', 'description', 'iri', 'linkedBookmark')
