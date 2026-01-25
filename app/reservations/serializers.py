from rest_framework import serializers
from .models import Reservation, Review


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'user', 'accommodation', 'reservation_date', 'status']


class SimpleReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'accommodation', 'reservation_date', 'status']


class ListReservationsSerializer(serializers.Serializer):
    reservations = SimpleReservationSerializer(many=True)


class CreateReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['user', 'accommodation', 'reservation_date', 'status']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'accommodation', 'user', 'rating', 'comment']


class SimpleReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'accommodation', 'rating', 'comment']


class ListReviewsSerializer(serializers.Serializer):
    reviews = SimpleReviewSerializer(many=True)


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['accommodation', 'user', 'rating', 'comment']