from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    
]
