from rest_framework import status
from .serializers import CustomAuthTokenSerializer, customTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomDiscardAuthToken(APIView):
    # for Discard Token
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({"message":"User token has been deleted."},status=status.HTTP_200_OK)
        except (AttributeError, ObjectDoesNotExist): # if there is not Token Exist for the current User
            return Response(status=status.HTTP_204_NO_CONTENT)


class CustomObtainAuthToken(ObtainAuthToken):
    # Getting a token for Login
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"token": token.key, "user_id": user.pk, "email": user.email}
        )


class CustomTokenObtainPairView(TokenObtainPairView):
    # Customizing JWT OutPut for create new JWT
    serializer_class = customTokenObtainPairSerializer