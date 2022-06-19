from csv import field_size_limit
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from blog.models import Category, Comment, Post, Tag


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "image", "like", "category"]


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "image", "like", "category"]


class PostRetrieveSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        exclude = ["create_dt"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


# class PostLikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ["like"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


# class CateTagSerializer(serializers.Serializer):
#     cateList = CategorySerializer(many=True)  ## list로 표현
#     tagList = TagSerializer(many=True)


class CateTagSerializer(serializers.Serializer):
    cateList = serializers.ListField(child=serializers.CharField())
    tagList = serializers.ListField(child=serializers.CharField())


class PostSerializerSub(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title"]


class CommentSerializerSub(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "update_dt"]


class PostSerializerDetail(serializers.Serializer):
    post = PostRetrieveSerializer()
    prevPost = PostSerializerSub()
    nextPost = PostSerializerSub()
    commentList = CommentSerializerSub(many=True)
