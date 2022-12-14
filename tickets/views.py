from rest_framework import generics

from account.permissions import IsAdminOrReadOnly
from . import serializers
from . import models as mod
from movies.models import  Movies

class TicketsView(generics.ListCreateAPIView):
    serializer_class = serializers.TicketSerializer
    queryset = mod.Tickets.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)        # автоматически заполняет поле owner_id


class TicketsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TicketSerializer
    queryset = mod.Tickets.objects.all()


class OrdersView(generics.ListCreateAPIView):
    serializer_class = serializers.OrdersSerializer
    queryset = mod.Orders.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)        # автоматически заполняет поле owner_id


class OrdersDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.OrdersSerializer
    queryset = mod.Orders.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)        # автоматически заполняет поле owner_id



class FeedbackView(generics.ListCreateAPIView):
    serializer_class = serializers.FeedbackSerializer
    queryset = mod.Feedback.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)        # автоматически заполняет поле owner_id



class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FeedbackSerializer
    queryset = mod.Feedback.objects.all()


class BookingView(generics.ListCreateAPIView):
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = mod.Booking.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)        # автоматически заполняет поле owner_id
        movie_id = self.kwargs['pk']


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = mod.Booking.objects.all()


class SeatsView(generics.ListCreateAPIView):
    serializer_class = serializers.SeatsSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = mod.Seats.objects.all()


class SeatsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.SeatsSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = mod.Seats.objects.all()


class TicketTypeView(generics.ListCreateAPIView):
    serializer_class = serializers.TicketTypeSerializer
    queryset = mod.TicketType.objects.all()


class TicketTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TicketTypeSerializer
    queryset = mod.TicketType.objects.all()


class ClubCardView(generics.ListCreateAPIView):
    serializer_class = serializers.ClubCardSerializer
    queryset = mod.ClubCard.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ClubCardDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ClubCardSerializer
    queryset = mod.ClubCard.objects.all()
