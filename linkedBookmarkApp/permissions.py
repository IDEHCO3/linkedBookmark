from rest_framework import permissions
from models import *


class IsOwnerOrReadOnlyResource(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        resource_id = view.kwargs.get('pk')
        try:
            user_id = LinkedBookmarkResource.objects.get(id=resource_id).user.id
            request.data['user'] = user_id
        except LinkedBookmarkResource.DoesNotExist:
            user_id = None
        return user_id == request.user.id


class IsOwnerOrReadOnlyResourceItem(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        resource_item_id = view.kwargs.get('pk')
        try:
            linkedBookmark = LinkedBookmarkItemResource.objects.get(id=resource_item_id).linkedBookmark
            user_id = linkedBookmark.user.id
            request.data['linkedBookmark'] = linkedBookmark.id
        except LinkedBookmarkItemResource.DoesNotExist:
            user_id = None

        return user_id == request.user.id

class IsOwnerOrReadOnlyResourceItemPost(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        resource_id = view.kwargs.get('resource_id')
        if resource_id is None:
            resource_id = request.data['linkedBookmark']

        try:
            user_id = LinkedBookmarkResource.objects.get(id=resource_id).user.id
            request.data['linkedBookmark'] = resource_id
        except LinkedBookmarkResource.DoesNotExist:
            user_id = None
        return user_id == request.user.id