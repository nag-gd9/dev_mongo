from rest_framework import serializers
from home.models import Musician, Album


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


        