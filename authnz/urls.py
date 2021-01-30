from django.urls import path

from authnz import views as authnz_views


urlpatterns = [
    path('authnz/register/', authnz_views.RegisterView.as_view(), name='register'),
    path('authnz/login/', authnz_views.LoginView.as_view(), name='login'),
]
