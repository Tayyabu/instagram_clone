from django.conf import settings
from django.urls import is_valid_path
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView,ListCreateAPIView
from accounts.serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from rest_framework.decorators import permission_classes, api_view

from api.pagination import PostPagination

# Create your views here.


class ListAndRegisterView(ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    pagination_class = PostPagination
    queryset = get_user_model().objects.all()

    def perform_create(self, serializer):
        user = serializer.save()
        # Give the user the global permission to add posts
        # This allows them to pass the initial check in CustomObjectPermissions
        add_perm = Permission.objects.get(codename="add_post")
        read_perm = Permission.objects.get(codename="view_post")
        user.user_permissions.add(add_perm)
        user.user_permissions.add(read_perm)




class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs) -> Response:

        refresh_token = request.COOKIES.get(settings.JWT_REFRESH_TOKEN_KEY)
        print(request.COOKIES)

        if refresh_token:

            data = request.data.copy()  # type: ignore
            data["refresh"] = refresh_token
            request._full_data = data  # This satisfies SimpleJWT's internal validation
        else:
            return Response(
                {"error": "No refresh token provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # 3. Let the parent class handle the actual validation/generation
        response = super().post(request, *args, **kwargs)

        # 4. If successful, hide the refresh token back in a cookie
        if response.status_code == 200:
            if "refresh" in response.data:  # type: ignore
                response.set_cookie(
                    settings.JWT_REFRESH_TOKEN_KEY,
                    response.data["refresh"],  # type: ignore
                    httponly=True,
                    samesite="None",
                    secure=True,  # Set to True in Production
                )
                del response.data["refresh"]  # type: ignore

        return response


class CookieTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            # pyright: ignore[reportOptionalMemberAccess]
            refresh_token = response.data.get("refresh")  # type: ignore

            response.set_cookie(
                key=settings.JWT_REFRESH_TOKEN_KEY,
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite="None",
            )
            # Remove tokens from response body so JS can't see them
            # type: ignore
            del response.data["refresh"]  # type: ignore

        return response
    


@api_view(["POST"])
def check_username(request):
    user = get_user_model().objects.filter(username=request.data.get("username"))
    
    
    if user.exists():
        return Response(
            {"message": "<h1 class='text-red-500 absolute'>User with username \"{}\" already exists</h1>".format(user.first().username)}  # type: ignore
        )
    return Response(
        {"message": "<h1 class='text-green-500 absolute'>Username is Availible</h1>"}
    )



@permission_classes([permissions.IsAuthenticated])
@api_view(["GET"])
def get_current_user(request) -> Response:

    serializer = UserSerializer(
        request.user
    )
        
    return Response(serializer.data)
