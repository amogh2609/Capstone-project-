from django.shortcuts import render
from rest_framework import generics,viewsets
from .serializers import MenuSerializer,BookingSerializer,UserSerializer
from .models import Menu,Booking
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticatedOrReadOnly] 

class MenuItemView(generics.ListCreateAPIView):
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class SingleMenuItemView (generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


@api_view()
@permission_classes([permissions.IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})