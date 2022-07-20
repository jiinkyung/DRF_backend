from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status

# Create your views here.
from .models import Vegan, Comment
from .serializers import CommentCreateSerializer, VeganSimpleSerializer, VeganDetailSerializer, CommentSerializer, VeganCreateSerializer

# 전체 식당목록 조회 / 등록
class VeganAPIView(APIView):
    def get(self, request):
        vegans = Vegan.objects.all()
        serializer = VeganSimpleSerializer(vegans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VeganCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 식당 상세 조회
class VeganDetailAPIView(APIView):
    def get(self, request, pk):
        vegan = get_object_or_404(Vegan, id=pk)
        serializer = VeganDetailSerializer(vegan)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 해당 글에 댓글쓰기
    def post(self, request, pk):
        post = get_object_or_404(Vegan, id= pk)
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save(post=post) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 전체 댓글 조회
class CommentAPIView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 댓글 상세 조회
class CommentDetailAPIView(APIView):
    def get(self, request, post_id):
        comments = get_object_or_404(Comment, id=post_id)
        serializer = CommentSerializer(comments)
        return Response(serializer.data, status=status.HTTP_200_OK)
