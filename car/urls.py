from django.urls import path

from car import views as car_views

urlpatterns = [
    path('car/list/', car_views.CarListView.as_view()),
    path('car_stock/list/', car_views.CarStockListView.as_view()),
    path('car/buy/', car_views.CarBuyView.as_view()),
    path('car/stock/', car_views.CarStockView.as_view()),
]
