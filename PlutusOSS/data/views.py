from rest_framework import viewsets
from data.models import Stock
from data.serializers import StockSerializer

class StockViewSet(viewsets.ModelViewSet):
    """ViewSet that represents Stock model"""
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

