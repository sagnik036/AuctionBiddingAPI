"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import permissions
from django.contrib import admin
from django.urls import path,include
import jwt
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="AUCTION_BIDDING API",
        default_version='v1',
        description="AUCTION BIDDING API BY SAGNIK BANIK",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
     path(
        'api/swagger/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
        name='schema-swagger-ui'
    ),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/',include('myapp.urls'))
]
