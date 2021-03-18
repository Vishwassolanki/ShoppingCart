from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('tracker', views.tracker, name="tracker"),
    path('login', views.login, name="login"),
    path('products/<int:myid>', views.products, name="products"),
    path('search', views.products, name="search"),
    path('cart', views.cart, name="cart"),
    path('wishlist', views.wishlist, name="wishlist"),
    path('orders', views.orders, name="orders"),
]
