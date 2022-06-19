# from django.urls import include, path
# from rest_framework import routers

# from api2.views import CommentViewSet, PostViewSet, UserViewSet

# router = routers.DefaultRouter()
# router.register(r"users", UserViewSet)
# router.register(r"post", PostViewSet)
# router.register(r"comment", CommentViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
# ]

from django.urls import path
from api2 import views

urlpatterns = [
    path("post/", views.PostListAPIView.as_view(), name="post-list"),
    path(
        "post/<int:pk>/",
        views.PostRetrieveAPIView.as_view(),
        name="post-detail",
    ),
    path("comment/", views.CommentCreateAPIView.as_view(), name="comment-list"),
]
