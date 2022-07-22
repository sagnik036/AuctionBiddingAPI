from .models import Auction
from rest_framework import serializers

class AuctionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = "__all__"

class AuctionBiddingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['id','current_bid_user_id','current_bid_price']