from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Reservation, Review
from app.permissions import UserIsLandlord, UserIsCustomer, CanViewReservation
from rest_framework.views import APIView
from . import serializers
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

class ListReservations(APIView):
    serializer_class = serializers.ListReservationsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [CanViewReservation] 

    @extend_schema(responses={200: serializers.ListReservationsSerializer})
    def get(self, request, format=None):
        query_set = Reservation.objects.all()
        reservation_data = self.serializer_class({"reservations": query_set}).data
        return Response(reservation_data)

class GetReservation(APIView):
    serializer_class = serializers.ReservationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [CanViewReservation]  

    @extend_schema(
        parameters=[OpenApiParameter(name='id', type=OpenApiTypes.INT, location=OpenApiParameter.QUERY, required=True)],
        responses={200: serializers.ReservationSerializer}
    )
    def get(self, request, format=None):
        reservation_id = request.query_params.get("id")
        try:
            reservation = Reservation.objects.get(id=reservation_id)
            reservation_data = self.serializer_class(reservation).data
            return Response(reservation_data)
        except Reservation.DoesNotExist:
            return Response({"detail": "Reservation not found."}, status=404)

class CreateReservation(APIView):
    serializer_class = serializers.CreateReservationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserIsCustomer]

    @extend_schema(
        request=serializers.CreateReservationSerializer,
        responses={201: serializers.ReservationSerializer, 400: None}
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            reservation = serializer.save(user=request.user)
            return Response({"reservation": serializers.ReservationSerializer(reservation).data}, status=201)
        return Response(serializer.errors, status=400)

class DeleteReservation(APIView):
    serializer_class = serializers.ReservationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserIsLandlord] 

    @extend_schema(
        parameters=[OpenApiParameter(name='id', type=OpenApiTypes.INT, location=OpenApiParameter.QUERY, required=True)],
        responses={204: None, 404: None}
    )
    def delete(self, request):
        reservation_id = request.query_params.get("id")
        try:
            reservation = Reservation.objects.get(id=reservation_id)
            reservation.delete()
            return Response(status=204)
        except Reservation.DoesNotExist:
            return Response(status=404)

class ListReviews(APIView):
    serializer_class = serializers.ListReviewsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [CanViewReservation] 

    @extend_schema(responses={200: serializers.ListReviewsSerializer})
    def get(self, request, format=None):
        query_set = Review.objects.all()
        review_data = self.serializer_class({"reviews": query_set}).data
        return Response(review_data)

class GetReview(APIView):
    serializer_class = serializers.ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [CanViewReservation]  

    @extend_schema(
        parameters=[OpenApiParameter(name='id', type=OpenApiTypes.INT, location=OpenApiParameter.QUERY, required=True)],
        responses={200: serializers.ReviewSerializer}
    )
    def get(self, request, format=None):
        review_id = request.query_params.get("id")
        try:
            review = Review.objects.get(id=review_id)
            review_data = self.serializer_class(review).data
            return Response(review_data)
        except Review.DoesNotExist:
            return Response({"detail": "Review not found."}, status=404)

class CreateReview(APIView):
    serializer_class = serializers.CreateReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserIsCustomer]  

    @extend_schema(
        request=serializers.CreateReviewSerializer,
        responses={201: serializers.ReviewSerializer, 400: None}
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            review = serializer.save(user=request.user)
            return Response({"review": serializers.ReviewSerializer(review).data}, status=201)
        return Response(serializer.errors, status=400)

class DeleteReview(APIView):
    serializer_class = serializers.ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserIsLandlord] 

    @extend_schema(
        parameters=[OpenApiParameter(name='id', type=OpenApiTypes.INT, location=OpenApiParameter.QUERY, required=True)],
        responses={204: None, 404: None}
    )
    def delete(self, request):
        review_id = request.query_params.get("id")
        try:
            review = Review.objects.get(id=review_id)
            review.delete()
            return Response(status=204)
        except Review.DoesNotExist:
            return Response(status=404)
