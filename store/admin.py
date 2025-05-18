from django.contrib import admin
from .models import Game, CartItem, Favorite, Order, Transaction

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'status')
    list_filter = ('status',)

admin.site.unregister(Order)
admin.site.register(Order, OrderAdmin)
admin.site.register(Game)
admin.site.register(CartItem)
admin.site.register(Favorite)
admin.site.register(Order)
admin.site.register(Transaction)
