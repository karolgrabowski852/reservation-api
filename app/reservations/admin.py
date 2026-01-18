from django.contrib import admin

# Register your models here.

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'accommodation', 'start_date', 'end_date')    
    readonly_fields = ('id',)

class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'landlord', 'rating')    
    readonly_fields = ('id',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'accommodation', 'user', 'rating')    
    readonly_fields = ('id',)
