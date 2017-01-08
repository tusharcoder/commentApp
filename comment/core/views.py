# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-01-08T13:24:36+05:30
# @Email:  tamyworld@gmail.com
# @Filename: views.py
# @Last modified by:   tushar
# @Last modified time: 2017-01-08T14:26:26+05:30



from django.shortcuts import render
from .models import Comment
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
# Create your views here.

#serializers
class CommentSerializer(serializers.Serializer):
    """serializer of the comment"""
    id=serializers.IntegerField(required=False)
    text = serializers.CharField(max_length=150)
    author = serializers.CharField(max_length=200)
    def create(self, validated_data):
        """Method to create the comment"""
        comment=Comment(**validated_data)
        comment.save()
        return comment
    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.content = validated_data.get('author', instance.author)
        instance.save()
        return instance

class CommentList(APIView):
    """List all comments ur create new"""

    def get(self,request,format=None):
        comments=Comment.objects.all()
        serializer=CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    """Detail view for the comment"""
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comment=self.get_object(pk)
        serializer=CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
