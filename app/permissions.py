from rest_framework import permissions
from app.users.models import User


class UserIsLandlord(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.LANDLORD
    
class UserIsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.CUSTOMER
    

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
    