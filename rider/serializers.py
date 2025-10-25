from django.utils import timezone
from rest_framework import serializers
from .models import User, Ride, RideEvent

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = '__all__'


class RideSerializer(serializers.ModelSerializer):
    id_rider = UserSerializer(read_only=True) # keep CRUD for Users separate
    id_driver = UserSerializer(read_only=True) # keep CRUD for Users separate
    todays_ride_events = serializers.SerializerMethodField()

    class Meta:
        model = Ride
        fields = '__all__'

    def get_todays_ride_events(self, ride):
        now = timezone.now()
        last_24_hours = now - timezone.timedelta(hours=24)
        events = ride.rideevent_set.filter(created_at__gte=last_24_hours)

        return RideEventSerializer(events, many=True).data
