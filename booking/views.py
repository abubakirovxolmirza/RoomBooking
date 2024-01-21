from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from .serializers import RoomSerializer
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


class RoomList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        today = timezone.now()

        rooms = Room.objects.all()
        available_rooms = rooms.filter(booking=False)
        reserved_rooms = rooms.filter(booking=True)

        serialized_available = RoomSerializer(available_rooms, many=True)
        serialized_reserved = RoomSerializer(reserved_rooms, many=True)

        data = {
            "available": serialized_available.data,
            "reserved": serialized_reserved.data,
            "date": today.strftime("%Y-%m-%d %H:%M:%S"),
        }

        return Response(data)


class BookRoomView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        room_name = request.data.get('room_name')
        start_time = request.data.get('start')
        end_time = request.data.get('end')

        try:
            room = Room.objects.get(name=room_name)
        except ObjectDoesNotExist:
            return Response({
                "message": f"{room_name} nomli hona topilmadi yoki mavjud emas xona nomi kiritildi!",
            }, status=status.HTTP_404_NOT_FOUND)

        if room.booking:
            available_from = room.end_time.strftime('%Y-%m-%d %H:%M:%S')
            return Response({
                "message": f"{room_name} honasi allaqachon boshqa bir mijoz tomonidan band qilingan!",
                "available_from": available_from
            }, status=status.HTTP_409_CONFLICT)
        else:
            room.booking = True
            room.start_time = start_time
            room.end_time = end_time
            room.save()
            serializer = RoomSerializer(room)
            return Response({
                "message": "Xona siz uchun muvaffaqiyatli band qilindi!",
                "room": serializer.data['id'],
                "room_name": serializer.data['name'],
                "start": serializer.data['start_time'],
                "end": serializer.data['end_time']
            }, status=status.HTTP_201_CREATED)


class RoomDetailView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, room_name):
        room = get_object_or_404(Room, name=room_name)
        is_free = not room.booking
        serializer = RoomSerializer(room)

        response_data = {
            "room": room.id,
            "room_name": room.name,
            "is_free": is_free,
            "description": f"{room.capacity} kishilik {room.description}",
        }
        return Response(response_data, status=status.HTTP_200_OK)

