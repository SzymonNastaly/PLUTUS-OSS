from data.models import Stock
from data.serializers import StockSerializer
from data.serializers import StockListSerializer
from data.my_permissions import IsAdminOrAuthenticatedReadOnly

from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from rest_framework.authtoken.models import Token


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


def signup(request):
    """Returns signup page (account creation)"""
    token = "notassigned"
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
#            return redirect('/api/')
    else:
        form = UserCreationForm()
    return render(request, 'data/signup.html', {'form': form, 'token': token})


def index(request):
    """Returns index/info page"""
    return render(request, 'data/index.html')
