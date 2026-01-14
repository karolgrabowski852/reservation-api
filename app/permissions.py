from urllib3 import request
from rest_framework import permissions
from app.users.models import User

def is_authenticated(request) -> bool:
    if not request.user or not request.user.is_authenticated:
        return False
    return True


class CanMakeReservation(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.CUSTOMER


class CanDeleteReservation(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [User.Role.LANDLORD, User.Role.CUSTOMER]
    

class CanDeleteAccommodation(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.LANDLORD


class CanCreateAccommodation(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.LANDLORD
    

class CanReviewAccommodation(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.CUSTOMER


class CanViewAccommodation(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [User.Role.CUSTOMER, User.Role.LANDLORD]
    
    
class CanViewReservation(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [User.Role.CUSTOMER, User.Role.LANDLORD]
    

class CanGiveAccomodationRating(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [User.Role.CUSTOMER]


class CanGiveUserRating(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [User.Role.LANDLORD, User.Role.CUSTOMER]
    