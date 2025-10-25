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
    ride_events = RideEventSerializer(source='rideevent_set', many=True, read_only=True)

    class Meta:
        model = Ride
        fields = '__all__'
