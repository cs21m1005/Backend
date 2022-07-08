from django.urls import path
from api import views
#from api.views import CartItemViews

urlpatterns = [
    path('customerapp', views.customerapp),
    path('Purchaseapp', views.Purchaseapp),
    #path('Shippingapp', views.Shippingapp),
]
