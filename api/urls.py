from django.urls import path

from .views import PostListCreateView, PostRetrieveUpdateDestroyView


urlpatterns = [
    path("posts/", view=PostListCreateView.as_view()),
    path("posts/<int:pk>/", view=PostRetrieveUpdateDestroyView.as_view()),
]
