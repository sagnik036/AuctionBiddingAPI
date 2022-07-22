from django.views import View
from .models import *


class AuctionInfo(View):
    @staticmethod
    def list_data(instance):
        result = {}
        if instance:
            result["id"] = instance.id
            result["name"] = instance.name
            result["start_price"] = instance.start_price
            if instance.is_active ==  True:
              result["status"] = "on_going"
            else:
              result["status"] = "ended"
        return result

    @staticmethod
    def details_data(instance):
        result = {}
        if instance:
            result["id"] = instance.id
            result["name"] = instance.name
            result["start_price"] = instance.start_price
            result["start_time"] = instance.start_time
            result["end_time"] = instance.end_time
            if instance.is_active ==  True:
              result["status"] = "on_going"
            else:
              result["status"] = "ended"
            result["winner_user_id"] = instance.winner_user_id
            result["current_bid_user_id"] = instance.current_bid_user_id
            result["current_bid_price"] = instance.current_bid_price
        return result


class AuctionBiddingInfo(View):
    @staticmethod
    def list_data(instance):
        result = {}
        if instance:
            result["id"] = instance.id
            result["current_bid_user_id"] = instance.current_bid_user_id
            result["current_bid_price"] = instance.current_bid_price
            # if instance.is_active ==  True:
            #   result["status"] = "on_going"
            # else:
            #   result["status"] = "ended"
        return result

    @staticmethod
    def details_data(instance):
        result = {}
        if instance:
            result["id"] = instance.id
            result["current_bid_user_id"] = instance.current_bid_user_id
            result["current_bid_price"] = instance.current_bid_price
            # if instance.is_active ==  True:
            #   result["status"] = "on_going"
            # else:
            #   result["status"] = "ended"
        return result