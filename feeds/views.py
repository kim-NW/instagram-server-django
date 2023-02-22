from django.shortcuts import render
from .serializers import FeedSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Feed


class MyFeed(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):  # Read
        feed = Feed.objects.all()

        # Serialize화 해줘야 -> 유저한테 보낼 수 있다.
        serializer = FeedSerializer(
          feed,
          many=True
        )

        return Response(serializer.data)
