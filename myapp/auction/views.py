from myapp.auction.info import AuctionInfo
from myapp.auction.services import AuctionServices
from .models import User
from .serializers import AuctionBiddingSerializers, AuctionSerializers
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from myapp.common.serializers.serializers import MasterListFilterBackend
from myapp.common.responses.error_response import FormatResponses
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from myproject.permission import *

class Auction(GenericAPIView):
    serializer_class = AuctionSerializers
    filter_backends = (MasterListFilterBackend,)
    permission_classes=[IsGetOrIsAuthenticated]
  
    @classmethod
    def get(cls, request):
        data = request.GET
        response = AuctionServices.fetch_profiles(data)
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    @classmethod
    def post(cls, request):
        validate_data = AuctionSerializers(data=request.data)
        is_valid = validate_data.is_valid()
        if is_valid:
            data = validate_data.validated_data
            instance = AuctionServices.save(data)
           
            response = {
                "result": instance.id,
                "message": "Profile Added successfully.",
            }
            status_code = status.HTTP_200_OK
        else:
            errors = FormatResponses.error_response(validate_data.errors)
            response = {"errors": errors}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(response, status=status_code)

class AuctionDetail(GenericAPIView):
    serializer_class = AuctionSerializers
    filter_backends = (MasterListFilterBackend,)
    permission_classes =[IsAdminUser]

    @classmethod
    def get(cls, request, pk):
        response = AuctionServices.fetchProfileById(pk)
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    @classmethod
    def put(cls, request, pk):
        validate_date = AuctionSerializers(data=request.data)
        is_valid = validate_date.is_valid()
        if is_valid:
            data = validate_date.validated_data
            AuctionServices.update(pk, data)
            response = {
                "message": "Updated Successfully"
            }
            status_code = status.HTTP_200_OK
            return Response(response, status=status_code)

        else:
            errors = FormatResponses.error_response(validate_date.errors)
            response = {
                "errors": errors
            }

            status_code = status.HTTP_400_BAD_REQUEST
            return Response(response, status_code)

    @classmethod
    def delete(cls, request, pk):
        AuctionServices.delete(pk)
        response = {
            "message": "Deleted Successfully"
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

class AuctionBidding(GenericAPIView):
    serializer_class = AuctionBiddingSerializers
    filter_backends = (MasterListFilterBackend,)
    permission_classes=[IsAuthenticatedOrReadOnly]
  
    @classmethod
    def get(cls, request, pk):
        response = AuctionServices.fetchProfileById(pk)
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    @classmethod
    def put(cls, request, pk):
        validate_date = AuctionBiddingSerializers(data=request.data)
        is_valid = validate_date.is_valid()
        if is_valid:
            data = validate_date.validated_data
            AuctionServices.bidupdate(pk, data)
            response = {
                "message": "Updated Successfully"
            }
            status_code = status.HTTP_200_OK
            return Response(response, status=status_code)

        else:
            errors = FormatResponses.error_response(validate_date.errors)
            response = {
                "errors": errors
            }

            status_code = status.HTTP_400_BAD_REQUEST
            return Response(response, status_code)
