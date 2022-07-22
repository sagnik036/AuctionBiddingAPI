from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('user/', include('myapp.user_management.urls'), name="user-login"),
    path('', include('myapp.auction.urls'), name="auction")

]
