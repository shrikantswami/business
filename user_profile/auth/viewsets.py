from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from user_profile.auth.serializer import LoginSerializer, RegisterSerializer


class LoginViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        try:
            print('creating user ')
            user_data = self.extract_user_detais(request)
            serializer = self.get_serializer(data=user_data)

            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            res = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }

            return Response({
                "user": serializer.data,
                "refresh": res["refresh"],
                "token": res["access"]
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(str(e))

    def extract_user_detais(self, request):
        try:
            data = {}
            data['username'] = request.data['email']['value'].split('@')[0]
            data['email'] = request.data['email']['value']
            data['password'] = request.data['password']['value']
            data['first_name'] = request.data.get('firstName',{}).get('value')
            data['middle_name'] = request.data.get('middleName',{}).get('value')
            data['last_name'] = request.data.get('lastName',{}).get('value')
            return data
        except Exception as e:
            print(str(e))
            return {}


class RefreshViewSet(ViewSet, TokenRefreshView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)