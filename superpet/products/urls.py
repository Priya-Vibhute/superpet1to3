from django.urls import path
from .views import ProductListView,ProductDetailView,royalCaninProducts,CategoryDetailView
from .views import search,ProductCreateView,ProductUpdateView,ProductDeleteView,ProductAdminView
urlpatterns = [
    path("",ProductListView.as_view(),name="products"),
    path("<int:pk>/",ProductDetailView.as_view(),name="productdetail"),
    path('royal-canin-products/',royalCaninProducts,name="royalcanin"),
    path('create-product/',ProductCreateView.as_view(),name="create-view"),
    path('update-product/<int:pk>/',ProductUpdateView.as_view(),name="update-product"),
    path('delete-product/<int:pk>/',ProductDeleteView.as_view(),name="delete-product"),
    path('product-admin/',ProductAdminView.as_view(),name="prduct-admin"),
    path("<slug:slug>/",CategoryDetailView.as_view(),name='category'),
    path('search',search,name='search'),
  
]