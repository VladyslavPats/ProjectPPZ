from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Game, CartItem, Order
from django.contrib.auth.decorators import login_required
from .models import Favorite

@login_required
def add_to_favorites(request, game_id):
    game = Game.objects.get(id=game_id)
    Favorite.objects.get_or_create(user=request.user, game=game)
    return redirect('game_list')

@login_required
def remove_from_favorites(request, game_id):
    Favorite.objects.filter(user=request.user, game__id=game_id).delete()
    return redirect('favorites')

@login_required
def favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'store/favorites.html', {'favorites': favorites})

@login_required
def add_to_favorites(request, game_id):
    game = Game.objects.get(id=game_id)
    Favorite.objects.get_or_create(user=request.user, game=game)
    return redirect('game_list')

@login_required
def remove_from_favorites(request, game_id):
    Favorite.objects.filter(user=request.user, game__id=game_id).delete()
    return redirect('favorites')

@login_required
def favorites(request):
    fav_games = Favorite.objects.filter(user=request.user)
    return render(request, 'store/favorites.html', {'favorites': fav_games})

@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/orders.html', {'orders': orders})

@login_required
def checkout(request):
    if request.method == 'POST':
        items = CartItem.objects.filter(user=request.user)
        if items:
            order = Order.objects.create(user=request.user)
            for item in items:
                order.games.add(item.game)
            order.save()
            items.delete()
        return redirect('orders')

@login_required
def add_to_cart(request, game_id):
    game = Game.objects.get(id=game_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, game=game)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    return render(request, 'store/cart.html', {'items': items})

def home(request):
    return render(request, 'store/home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def game_list(request):
    query = request.GET.get('q')
    if query:
        games = Game.objects.filter(title__icontains=query)
    else:
        games = Game.objects.all()
    return render(request, 'store/game_list.html', {'games': games, 'query': query})


def game_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'store/game_detail.html', {'game': game})
