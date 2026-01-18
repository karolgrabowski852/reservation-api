from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'rate', 'rates_count')
    readonly_fields = ('id', 'rate', 'rates_count')