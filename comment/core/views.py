# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-01-08T13:24:36+05:30
# @Email:  tamyworld@gmail.com
# @Filename: views.py
# @Last modified by:   tushar
# @Last modified time: 2017-01-08T13:54:52+05:30



from django.shortcuts import render
from .models import Comment
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

#serializers
class CommentSerializer(serializers.Serializer):
    """serializer of the comment"""
    text = serializers.CharField(max_length=150)
    author = serializers.CharField(max_length=200)

class CommentList(APIView):
    """List all comments ur create new"""
    def get(self,request,format=None):
        comments=Comment.objects.all()
        serializer=CommentSerializer(comments, many=True)
        return Response(serializer.data)
