from django.urls import include, path
from rest_framework import routers
from home import views

router = routers.DefaultRouter()
router.register(r'musician', views.MusicianViewSet)
router.register(r'album', views.AlbumViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include((router.urls, 'DRF_urls'))),
]