from rest_framework.serializers import ModelSerializer, CharField, EmailField
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "image",'email','bio']


class RegisterSerializer(ModelSerializer):
    password = CharField(write_only=True)
    username = CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="This user already exists."
            )
        ]
    )
    email = EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="Email already registered."
            )
        ],
    )

    class Meta:
        model = User
        fields = ("username", "email", "password",'id','image')

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)  # type: ignore
