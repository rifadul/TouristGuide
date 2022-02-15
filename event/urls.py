from django.urls import path
from .views import TouristEventView,event_profile_view,event_requriement,payment,payment_status

urlpatterns = [
path('create-event/',TouristEventView,name='create-event'),
path('profile/',event_profile_view,name='profile'),
path('event-requriement/',event_requriement,name='event-requriementfile'),
path('payment/', payment,name='payment'),
path('status/', payment_status,name='payment_status')
]