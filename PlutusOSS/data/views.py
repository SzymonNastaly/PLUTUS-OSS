from rest_framework import viewsets
from data.models import Stock
from data.serializers import StockSerializer
from data.serializers import StockListSerializer

class StockViewSet(viewsets.ModelViewSet):
    """ViewSet that represents Stock model"""
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    list_serializer_class = StockListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            if hasattr(self, 'list_serializer_class'):
                return self.list_serializer_class

        return super(StockViewSet, self).get_serializer_class()

