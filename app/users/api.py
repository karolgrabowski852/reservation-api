from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from app.permissions import UserIsLandlord, UserIsCustomer
from adrf.views import APIView
from . import serializers 
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from asgiref.sync import sync_to_async
class ListUsers(APIView):
    serializer_class = serializers.ListUsersSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
            responses={200: serializers.ListUsersSerializer}
        )
    async def get(self, request, format=None):
        query_set = [user async for user in User.objects.all()]
        user_data = await self.serializer_class({"users":query_set}).adata
        return Response(user_data)
    

class GetUserProfile(APIView):
    serializer_class = serializers.UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticated]

    @extend_schema(
            parameters=[
                OpenApiParameter(
                    name='id', 
                    type=OpenApiTypes.INT,
                    location=OpenApiParameter.QUERY,
                    required=True
                ),
            ],
            responses={200: serializers.UserSerializer}
        )
    async def get(self, request, format=None):
        user_id = request.query_params.get("id")
        current_user = request.user
        if current_user.role in [User.Role.LANDLORD, User.Role.CUSTOMER] and str(current_user.id) != user_id:
            return Response({"detail": "You do not have permission to perform this action."}, status=403)

        user = request.user
        try:
            user = await User.objects.aget(id=user_id)
        except (User.DoesNotExist, ValueError):
            return Response({"detail": "User not found."}, status=404)
        
        user_data = await self.serializer_class(user).adata
        return Response(user_data)


class DeleteUser(APIView):
    serializer_class = serializers.DeleteUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
            parameters=[
                OpenApiParameter(
                    name='id', 
                    type=OpenApiTypes.INT, 
                    location=OpenApiParameter.QUERY,
                    required=True
                ),
            ],
            responses={201: None, 400: None, 404: None}
        )
    async def delete(self, request):
        user_id = request.query_params.get("id")
        try:
            user = await User.objects.aget(id=user_id)
            await user.adelete()
            return Response(status=201)
        except User.DoesNotExist:
            return Response(status=404)
        

class CreateUser(APIView):
    serializer_class = serializers.CreateUserSerializer

    
    @extend_schema(
            request=serializers.CreateUserSerializer,
            responses={201: serializers.UserSerializer, 400: None}
        )
    async def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if await sync_to_async(serializer.is_valid)():
            user = await serializer.asave()
            return Response({"user": await serializers.UserSerializer(user).adata}, status=201)
        else:
            return Response(serializer.errors, status=400)