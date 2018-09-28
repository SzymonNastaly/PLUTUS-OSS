from rest_framework import serializers
from data.models import Stock

class StockSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes Stock model with all attributes"""
    class Meta:
        model = Stock
        fields = ('url','name', 'ticker', 'current_liab', 'equity', 'total_assets',
                  'revenue12', 'revenue13', 'revenue14', 'revenue15', 'revenue16',
                  'ebit', 'netincome12', 'netincome13', 'netincome14', 'netincome15',
                  'netincome16', 'free_cashflow', 'eps12', 'eps13', 'eps14', 'eps15',
                  'eps16', 'eps_e', 'total_dividend', 'dividend_ps')

class StockListSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes a list of the Stock model with a few attributes"""
    class Meta:
        model = Stock
        fields = ('url', 'id','name', 'ticker')
