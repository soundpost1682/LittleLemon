from django.shortcuts import render

from rest_framework import generic
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generic.ListCreateView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerialier

class SingleMenuItemView(generic.RetrieveUpdateAPIView, generic.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerialier

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    Permission_classes = [permissions.IsAuthenticated]