from django.contrib import admin
from .models import User, Ride, RideEvent

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role')
    list_filter = ('role',)
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('get_rider_first_name', 'get_driver_first_name', 'status')
    list_filter = ('status',)
    search_fields = ('id_rider__first_name', 'id_rider__last_name', 'id_driver__first_name', 'id_driver__last_name', 'status')

    def get_rider_first_name(self, obj):
        return f'{obj.id_rider.first_name} {obj.id_rider.last_name}'
    get_rider_first_name.short_description = 'Rider'

    def get_driver_first_name(self, obj):
        return f'{obj.id_driver.first_name} {obj.id_driver.last_name}'
    get_driver_first_name.short_description = 'Driver'


@admin.register(RideEvent)
class RideEventAdmin(admin.ModelAdmin):
    list_display = ('ride', 'description', 'created_at')
    search_fields = ('ride__id_rider__first_name', 'ride__id_rider__last_name', 'ride__id_driver__first_name', 'ride__id_driver__last_name')
