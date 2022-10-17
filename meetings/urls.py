from django.urls import path
from . import views

urlpatterns = [
    path('<int:meeting_id>', views.details, name='details'),
    path('rooms', views.rooms, name='rooms'),
    path('new', views.new, name='new')
]