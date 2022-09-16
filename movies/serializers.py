import datetime
import pytz
from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import (Cinemas, Movies, ShowTime,
                     Rooms, RoomsFormat, MoviesCategory)

utc = pytz.UTC

class CategoryListSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = MoviesCategory
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['movies'] = MovieSerializer(instance.movies.all(), many=True).data
        return representation



class CinemasListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cinemas
        fields = ('id', 'name', 'cinemas_picture', 'contacts')

    def validate(self, attrs):
        if attrs['contacts'][:4] == '+996' or attrs['contacts'][0] == '0':
            return attrs
        else:
            raise ValidationError('Value should start with "+996" or "0"')


class CinemasDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cinemas
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    movie_status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'

    @staticmethod
    def get_movie_status(obj):

        now = datetime.date.today()

        if obj.beginning_of_movie <= now <= obj.ending_of_movie:
            obj.movie_status = 'current'
            return obj.movie_status

        if obj.beginning_of_movie > now:
            obj.movie_status = 'upcoming'
            return obj.movie_status


class ShowTimeSerializer(serializers.ModelSerializer):

    is_active = serializers.SerializerMethodField()

    class Meta:
        model = ShowTime
        fields = '__all__'

    @staticmethod
    def get_is_active(obj):
        end_time = obj.end_time.replace(tzinfo=utc)
        a = datetime.datetime.now()
        now = a.replace(tzinfo=utc)
        if now > end_time:
            obj.is_active = False
            obj.save()
        return obj.is_active


class RoomsFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomsFormat
        fields = '__all__'


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'