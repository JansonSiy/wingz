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
    id_rider = UserSerializer(read_only=True)
    id_driver = UserSerializer(read_only=True)
    todays_ride_events = serializers.SerializerMethodField()

    class Meta:
        model = Ride
        fields = '__all__'

    def get_todays_ride_events(self, ride):
        events = ride.rideevent_set.all()
        return RideEventSerializer(events, many=True).data
