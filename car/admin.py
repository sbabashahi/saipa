from django.contrib import admin

from car.models import Car, CarStock, CarSold


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    search_fields = ('name',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(CarStock)
class CarStockAdmin(admin.ModelAdmin):
    fields = ('car', 'price', 'total', 'date', 'total_sold',)
    list_display = ('car', 'price', 'total', 'date', 'total_sold',)
    search_fields = ('car__name',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(CarSold)
class CarSoldAdmin(admin.ModelAdmin):
    fields = ('car_stock', 'user', 'count')
    list_display = ('car_stock', 'user', 'count')
    search_fields = ('car__name', 'user__username')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
