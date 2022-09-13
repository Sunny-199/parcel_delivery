from django.urls import path
from django.urls import include
from .views import DashboardView, ShipmentsView, address_view, TicketsView, DetailView
from users import views
urlpatterns = [
    path("account/", include("allauth.urls")),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("shipments/", ShipmentsView.as_view(), name="shipments"),
    path("addresses/", address_view, name="addresses"),
    path("tickets/", TicketsView.as_view(), name="tickets"),
    path("detail/", DetailView.as_view(), name="detail"),
    path('contact', views.contact, name='contacts'),
    path('add_address', views.Address, name='contact')
]
