import datetime
from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from . import serializers
from . import models as mod
from account.permissions import IsAdminOrReadOnly

class CategoryView(ModelViewSet):
    queryset = mod.MoviesCategory.objects.all()
    permission_classes = (IsAdminOrReadOnly,)

    def get_serializer_class(self):
        return serializers.CategoryListSerializer
    
    
    

class CinemasView(generics.ListCreateAPIView):
    serializer_class = serializers.CinemasListSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = mod.Cinemas.objects.all()


class CinemasDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CinemasDetailSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = mod.Cinemas.objects.all()


class MovieView(generics.ListCreateAPIView):
    serializer_class = serializers.MovieSerializer
    queryset = mod.Movies.objects.filter(ending_of_movie__gt=datetime.datetime.now())
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ('category', 'name',)
    search_fields = ('name',)
 


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MovieSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = mod.Movies.objects.all()


class ShowTimeView(generics.ListCreateAPIView):
    serializer_class = serializers.ShowTimeSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = mod.ShowTime.objects.filter(is_active=True)


class ShowTimeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ShowTimeSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = mod.ShowTime.objects.all()


class RoomsView(generics.ListCreateAPIView):
    serializer_class = serializers.RoomsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = mod.Rooms.objects.all()


class RoomsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RoomsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = mod.Rooms.objects.all()


class RoomsFormatView(generics.ListCreateAPIView):
    serializer_class = serializers.RoomsFormatSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = mod.RoomsFormat.objects.all()


class RoomsFormatDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RoomsFormatSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = mod.RoomsFormat.objects.all()
