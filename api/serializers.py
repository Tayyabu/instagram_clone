from rest_framework.serializers import ModelSerializer, SlugRelatedField, RelatedField
from accounts.serializers import UserSerializer
from api.models import Post


class AuthorField(RelatedField):
    def to_representation(self, value):

        return f"{value.username}"


class PostSerializer(ModelSerializer):
    author = AuthorField(read_only=True)

    def create(self, validated_data) -> Post:
        return Post.objects.create(**validated_data)

    class Meta:
        model = Post
        fields = "__all__"
