from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


v1router = DefaultRouter()

v1router.register('posts', PostViewSet, basename='posts')
v1router.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                  basename='comments')
v1router.register('groups', GroupViewSet, basename='groups')
v1router.register('follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('v1/', include(v1router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
