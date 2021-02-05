from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from home.serializers import MusicianSerializer, AlbumSerializer
from .models import Musician, Album
from rest_framework import authentication


# Create your views here.

class MusicianViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




