from django.urls import path, include
from . import views
from .views import profile_view, sign_up, cart, AddToCartView

urlpatterns = [
    path(r'<slug:slug>/', views.PostListView.as_view(), name="post_list"),
    path('profile', profile_view, name="profile"),
    path('register', sign_up, name='register'),
    path('cart', cart, name='cart'),
    path('add_to_cart/<int:post_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('', views.home, name='home'),

]
