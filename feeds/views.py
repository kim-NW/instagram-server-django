from django.shortcuts import render
from .serializers import FeedSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from .models import Feed
from users.models import User

# 전체 게시글을 불러오는 API


class MyFeed(APIView):

    # permission_classes = [IsAuthenticated]

    def get(self, request):  # Read
        feed = Feed.objects.all()

        # Serialize화 해줘야 -> 유저한테 보낼 수 있다.
        serializer = FeedSerializer(
            feed,
            many=True
        )

        return Response(serializer.data)


# 특정 username을 기반으로 게시글을 불러오는 API

class SelectFeed(APIView):

    # permission_classes = [IsAuthenticated]

    def get(self, request, username):
        print("username", username)

        user = User.objects.get(username=username)
        print("user_id", user.id)

        user_feeds = Feed.objects.filter(user_id=user.id)
        print("user_feeds", user_feeds)

        serializer = FeedSerializer(user_feeds, many=True)

        return Response(serializer.data)