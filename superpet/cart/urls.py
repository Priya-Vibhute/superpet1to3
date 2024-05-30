from django.urls import path
from . import views
urlpatterns = [
    path("add-to-cart/<int:productId>/",views.add_to_cart,name="add-to-cart"),
    path("",views.cart,name="cart"),
    path("remove-from-cart/<int:cartItemId>/",views.remove_from_cart,name="remove-from-cart"),
    path("update-quantity/<int:cartItemId>/",views.update_cart,name="update-cart"),
    path("checkout/",views.checkout,name="checkout"),
    path("payment/<str:orderId>/",views.payment,name="payment"),
    path("success/<str:orderId>/",views.success,name="success")
    
]

