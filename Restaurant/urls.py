from django.urls import path
from . import views

urlpatterns = [

path('api/menu/', views.MenuItemsView.as_view()),
path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),


path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('menu/', views.menu, name='menu'),
path('book/', views.book, name='book'),
path('bookings/', views.bookings, name='bookings'),
]