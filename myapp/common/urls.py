from django.urls import path, include


urlpatterns = [
    path(
        'media/',
        include("myapp.common.manage_media.urls"),
        name="media_urls"
    ),
]
