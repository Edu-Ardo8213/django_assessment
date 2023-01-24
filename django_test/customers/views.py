from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from common.permissions import IsSuperAdminPermission
from .serializers import CustomerModelSerializer
from .models import Customer


class CustomerModelViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "email"]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "create", "destroy"]:
            self.permission_classes = [IsSuperAdminPermission]
        return super().get_permissions()