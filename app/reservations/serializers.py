
from rest_framework import serializers
from .models import Reservation, Review, Accommodation


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

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
        fields = ['accommodation', 'reservation_date', 'status']


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

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
        fields = ['accommodation', 'rating', 'comment']


class AccommodationSerializer(serializers.ModelSerializer):
    landlord = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Accommodation
        fields = ['id', 'name', 'location', 'description', 'landlord', 'rating']


class SimpleAccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation
        fields = ['id', 'name', 'location', 'rating']


class ListAccommodationsSerializer(serializers.Serializer):
    accommodations = SimpleAccommodationSerializer(many=True)


class CreateAccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation
        # landlord set from request
        fields = ['name', 'location', 'description']

