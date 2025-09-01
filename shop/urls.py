from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryRetrieveUpdateDeleteView,
    ProductListCreateView,
    ProductRetrieveUpdateDeleteView,
    RatingCreateView,
    RatingListView,
    CartListView,
    CartAddView,
    CartUpdateView,
    CartRemoveView,
    OrderCheckoutView,
    OrderListView,

)

urlpatterns = [
    # Categories
    path("categories/", CategoryListCreateView.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", CategoryRetrieveUpdateDeleteView.as_view(), name="category-detail"),

    # Products
    path("products/", ProductListCreateView.as_view(), name="product-list-create"),
    path("products/<int:pk>/", ProductRetrieveUpdateDeleteView.as_view(), name="product-detail"),



    # Ratings
    path("products/<int:pk>/rate/", RatingCreateView.as_view(), name="product-rate"),
    path("products/<int:pk>/ratings/", RatingListView.as_view(), name="product-ratings"),

    # Cart
    path("cart/", CartListView.as_view(), name="cart-list"),
    path("cart/add/", CartAddView.as_view(), name="cart-add"),
    path("cart/update/<int:pk>/", CartUpdateView.as_view(), name="cart-update"),
    path("cart/remove/<int:pk>/", CartRemoveView.as_view(), name="cart-remove"),

    # Orders
    path("orders/checkout/", OrderCheckoutView.as_view(), name="order-checkout"),
    path("orders/", OrderListView.as_view(), name="order-list"),
]
