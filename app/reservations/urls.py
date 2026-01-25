from django.urls import path
from .api import (
    ListReservations, GetReservation, CreateReservation, DeleteReservation,
    ListReviews, GetReview, CreateReview, DeleteReview
)

urlpatterns = [
    path('reservations/', ListReservations.as_view(), name='reservation-list'),
    path('reservations/get/', GetReservation.as_view(), name='reservation-get'),
    path('reservations/create/', CreateReservation.as_view(), name='reservation-create'),
    path('reservations/delete/', DeleteReservation.as_view(), name='reservation-delete'),
    path('reviews/', ListReviews.as_view(), name='review-list'),
    path('reviews/get/', GetReview.as_view(), name='review-get'),
    path('reviews/create/', CreateReview.as_view(), name='review-create'),
    path('reviews/delete/', DeleteReview.as_view(), name='review-delete'),
]