import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import User, Ride, RideEvent
from .serializers import UserSerializer, RideSerializer, RideEventSerializer
from .permissions import IsAdminUserRole
from .utils import calculate_pickup_distance

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUserRole]


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAdminUserRole]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'id_rider__email']
    ordering_fields = ['pickup_time', 'pickup_distance']
    ordering = ['pickup_time']
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(status='pickup')

        latitude = self.request.query_params.get('latitude')
        longitude = self.request.query_params.get('longitude')

        if latitude and longitude:
            try:
                latitude = float(latitude)
                longitude = float(longitude)

                for ride in queryset:
                    ride.pickup_distance = calculate_pickup_distance(
                        ride.pickup_latitude,
                        ride.pickup_longitude,
                        latitude,
                        longitude
                    )
                    ride.save()
            except ValueError:
                logger.error("Error: Cannot convert latitude/longitude to float.")
                pass

        return queryset

class RideEventViewSet(viewsets.ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
    permission_classes = [IsAdminUserRole]
