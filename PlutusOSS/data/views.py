from data.models import Stock
from data.serializers import StockSerializer
from data.serializers import StockListSerializer
from data.my_permissions import IsAdminOrAuthenticatedReadOnly

from rest_framework import viewsets


class StockViewSet(viewsets.ModelViewSet):
    """ViewSet that represents Stock model"""
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAdminOrAuthenticatedReadOnly,)
    list_serializer_class = StockListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            if hasattr(self, 'list_serializer_class'):
                return self.list_serializer_class

        return super(StockViewSet, self).get_serializer_class()
