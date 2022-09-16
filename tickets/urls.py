from django.urls import path

from . import views

urlpatterns = [
    path('tickets/', views.TicketsView.as_view()),
    path('tickets/<int:pk>/', views.TicketsDetailView.as_view()),
    path('orders/', views.OrdersView.as_view()),
    path('orders/<int:pk>/', views.OrdersDetailView.as_view()),
    path('feedbacks/', views.FeedbackView.as_view()),
    path('feedbacks/<int:pk>/', views.FeedbackDetailView.as_view()),
    path('booking/', views.BookingView.as_view()),
    path('booking/<int:pk>/', views.BookingDetailView.as_view()),
    path('seats/', views.SeatsView.as_view()),
    path('seats/<int:pk>/', views.SeatsDetailView.as_view()),
    path('type/', views.TicketTypeView.as_view()),
    path('type/<int:pk>/', views.TicketTypeDetailView.as_view()),
    path('club-card/', views.ClubCardView.as_view()),
    path('club-card/<int:pk>/', views.ClubCardDetailView.as_view()),
]