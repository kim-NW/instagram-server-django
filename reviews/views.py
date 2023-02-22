from django.shortcuts import render
from .serializers import ReviewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Review


class MyReview(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):  # Read
        review = Review.objects.all()

        # Serialize화 해줘야 -> 유저한테 보낼 수 있다.
        serializer = ReviewSerializer(
          review,
          many=True
        )

        return Response(serializer.data)
