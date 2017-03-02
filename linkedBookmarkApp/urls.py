
from django.conf.urls import include,  url
from rest_framework.urlpatterns import format_suffix_patterns
from linkedBookmarkApp import views

urlpatterns = [
    url(r'^linked-resources/$', views.ResourceList.as_view(), name='resource-list'),
    url(r'^linked-resources/(?P<pk>\d+)/$', views.ResourceDetail.as_view(), name='resource-detail'),
    url(r'^linked-resources-context/', views.ResourceContext.as_view(), name='resource-context'),

    url(r'^linked-resources-items/$', views.ResourceItemList.as_view(), name='resource-item-list'),
    url(r'^linked-resources-items/(?P<pk>\d+)/$', views.ResourceItemDetail.as_view(), name='resource-item-detail'),
    url(r'^linked-resources-items-context/', views.ResourceItemContext.as_view(), name='resource-item-context'),

    url(r'^linked-resources/(?P<resource_id>\d+)/items/$', views.ResourceItemList.as_view(), name='resource-list'),
    url(r'^linked-resources/(?P<resource_id>\d+)/items/(?P<pk>\d+)/$', views.ResourceItemDetail.as_view(), name='resource-detail'),
]