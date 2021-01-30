from django.urls import path

from car import views as car_views


urlpatterns = [
    path('car/list/', car_views.CarListView.as_view(), name='car_list'),
    path('car_stock/list/', car_views.CarStockListView.as_view(), name='car_stock_list'),
    path('car/buy/', car_views.CarBuyView.as_view(), name='car_buy'),
    path('car/sold_list/', car_views.CarSoldListView.as_view(), name='car_sold_list'),
]
