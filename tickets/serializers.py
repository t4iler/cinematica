from unicodedata import name
from rest_framework import serializers

from movies.models import Movies

from . import models as mod


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = mod.Tickets
        fields = '__all__'
        read_only_fields = ["price"]

    def validate(self, data):
        seats = data.get('seats')
        show_time = data.get('show_time')
        if mod.Booking.objects.filter(seats=seats, show_time=show_time).exists():

            raise serializers.ValidationError('This seat is already reserved.')

        return data


class OrdersSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    total_price = serializers.SerializerMethodField('get_total_price')

    class Meta:
        model = mod.Orders
        fields = '__all__'

    @staticmethod
    def get_total_price(obj):
        tickets = mod.Tickets.objects.filter(orders=obj.id)
        total_price = 0
        for ticket in tickets:

                total_price += ticket.price

        return total_price


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    movie = serializers.ReadOnlyField(source='movies.name')
    class Meta:
        model = mod.Feedback
        fields = '__all__'

    


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = mod.Booking
        fields = '__all__'

    def validate(self, data):
        seats = data.get('seats')
        show_time = data.get('show_time')
        if mod.Booking.objects.filter(seats=seats, show_time=show_time).exists():

            raise serializers.ValidationError('This seat is already reserved.')

        return data


class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = mod.Seats
        fields = '__all__'


class ClubCardSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = mod.ClubCard
        fields = '__all__'

    def get_balance(self, obj):
        orders = mod.Tickets.objects.filter(user=obj.user)
        balance = 0
        for i in orders:
            balance += i.price
        if balance > 5000:
            obj.discount = 3
        if balance > 7000:
            obj.discount = 5
        if balance > 10000:
            obj.discount = 7
        obj.save()
        return balance


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = mod.TicketType
        fields = '__all__'