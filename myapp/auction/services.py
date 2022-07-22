from django.db.models import Q
from myapp.common.repos.services import FetchServices, SaveServices
from .info import *


class AuctionServices(View):
    @staticmethod
    def fetch_profiles(data):
        # Fetching pagination information
        page_size = data.get("page_size")
        page_number = data.get("page")

        # Making Filter queries
        filter_query = AuctionServices.add_filter_queries(data)
        # Adding Search Queries
        filter_query = AuctionServices.add_search_queries(
            data,
            filter_query
        )
        # Making Order Queries
        order_query = AuctionServices.add_order_queries(data)
        # Fetching related instances
        instances = FetchServices.all_instances(
            "myapp",
            "Auction",
            filter_query=filter_query,
            order_query=order_query,
            page_size=page_size,
            page_number=page_number
        )
        # Making response output
        result = [AuctionInfo.list_data(instance) for instance in instances]
        return result

    @staticmethod
    def fetchProfileById(instance_id):
        instance = FetchServices.instance_by_id(
            "myapp",
            "Auction",
            instance_id,

        )

        result = AuctionInfo.details_data(instance)
        return result

    @staticmethod
    def save(data):
        columns = {
            "name": data.get("name"),
            "start_price": data.get("start_price"),
            "start_time": data.get("start_time"),
            "end_time": data.get("end_time"),
            "is_active": data.get("is_active")
        }

        instance = SaveServices.save_instance(
            "myapp",
            "Auction",
            columns
        )
        return instance

    @staticmethod
    def update(instance_id, data):
        columns = {
            "name": data.get("name"),
            "start_price": data.get("start_price"),
            "start_time": data.get("start_time"),
            "end_time": data.get("end_time"),
            "is_active": data.get("is_active")
        }

        filter_query = Q(
            id=instance_id
        )

        instance = SaveServices.update_instance(
            "myapp",
            "Auction",
            filter_query,
            columns,
        )

        return instance

    @staticmethod
    def bidupdate(instance_id, data):
        columns = {
            "current_bid_price": data.get("current_bid_price"),
            "current_bid_user_id": data.get("current_bid_user_id")
        }

        filter_query = Q(
            id=instance_id
        )

        instance = SaveServices.update_instance(
            "myapp",
            "Auction",
            filter_query,
            columns,
        )

        return instance

    @staticmethod
    def delete(instance_id):
        filter_query = Q(
            id=instance_id
        )

        SaveServices.delete_instances(
            "myapp",
            "Auction",
            filter_query
        )

        return True

    @staticmethod
    def add_filter_queries(data):
        filter_query = Q()
        return filter_query

    @staticmethod
    def add_search_queries(data, filter_query):
        search = data.get("search")
        if search:
            filter_query.add(
                Q(name__icontains=search),
                Q.AND
            )
        return filter_query

    @staticmethod
    def add_order_queries(data):
        order_query = ["id"]
        return order_query
