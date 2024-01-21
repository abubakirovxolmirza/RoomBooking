from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import SignupSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        user_instance = User.objects.get(username=request.data['username'])
        response_data = {
            'message': 'Siz muvaffaqiyatli royhatdan otdingiz'
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
