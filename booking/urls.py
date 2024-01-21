from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.RoomList.as_view(), name='room_list'),
    path('book/room/', views.BookRoomView.as_view(), name='book_room'),
    path('room/<str:room_name>/', views.RoomDetailView.as_view(), name='room_details'),
]
