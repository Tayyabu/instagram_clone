from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from rest_framework import permissions
from . import serializers
from . import models
from .permissions import IsAuthorOrReadOnly, CustomObjectPermissions
from rest_framework_guardian import filters
from .pagination import PostPagination
# Create your views here.


class PostListCreateView(ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    pagination_class = PostPagination
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.filter(is_published=True)

    def perform_create(self, serializer):
        # This replaces your manual .post() logic
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PostSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthorOrReadOnly,
    ]
    queryset = models.Post.objects.all()
