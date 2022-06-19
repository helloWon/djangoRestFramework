from collections import OrderedDict
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    GenericAPIView,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from api2.serializers import (
    CateTagSerializer,
    CommentSerializer,
    # PostLikeSerializer,
    PostListSerializer,
    PostRetrieveSerializer,
    PostSerializer,
    PostSerializerDetail,
)
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response
from blog.models import Category, Comment, Post, Tag


class CateTagAPIView(APIView):
    def get(self, request, *args, **kwargs):
        cateList = Category.objects.all()
        tagList = Tag.objects.all()

        data = {"cateList": cateList, "tagList": tagList}
        serializer = CateTagSerializer(instance=data)
        return Response(serializer.data)


class PostPageNumberPagination(PageNumberPagination):
    page_size = 3
    # page_size_query_param = "page_size"
    # max_page_size = 1000
    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("postList", data),
                    ("pageCnt", self.page.paginator.num_pages),
                    ("CurPage", self.page.number),
                ]
            )
        )


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPageNumberPagination

    def get_serializer_context(self):
        return {
            "request": None,
            "format": self.format_kwarg,
            "view": self,
        }  # DRF ImageField

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        prevInstance, nextInstance = get_prev_next(instance)
        commentList = instance.comment_set.all()
        data = {
            "post": instance,
            "prevPost": prevInstance,
            "nextPost": nextInstance,
            "commentList": commentList,
        }
        serializer = self.get_serializer(instance=data)
        return Response(serializer.data)

    def like(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()
        return Response(instance.like)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
