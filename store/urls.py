from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('games/', views.game_list, name='game_list'),
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:game_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('favorites/', views.favorites, name='favorites'),
    path('favorites/add/<int:game_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:game_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', views.favorites, name='favorites'),
    path('add-to-favorites/<int:game_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove-from-favorites/<int:game_id>/', views.remove_from_favorites, name='remove_from_favorites'),

]