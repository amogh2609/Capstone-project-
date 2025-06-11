from django.shortcuts import render
from rest_framework import generics,viewsets
from .serializers import MenuSerializer,BookingSerializer,UserSerializer
from .models import Menu,Booking
from django.contrib.auth.models import User
from rest_framework import permissions

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView (generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
