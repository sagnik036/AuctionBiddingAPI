from django import views
from django.contrib import admin
from django.urls import include, path
import jwt
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.authentication import JWTAuthentication


from .import views

urlpatterns = [
    path(
        'auction/list', 
        views.Auction.as_view(), 
        name="Auction"
    ),

    path(
        'auction/status/<int:pk>', 
         views.AuctionDetail.as_view(),
         name="Auction"
    ),

    path(
        'auction/bidding/<int:pk>', 
        views.AuctionBidding.as_view(), 
        name="AuctionBid"
    ),

]
