from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from .serializers import UserProfileSerializer, BlogPostSerializer
from account.models import Account
from post.models import BlogPost
from . import permissions
# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = UserProfileSerializer
    queryset = Account.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)


class BlogPostViewSet(viewsets.ModelViewSet):
    """Handles creating. reading and updating users blog."""
    authentication_classes = (TokenAuthentication,)
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        serializer.save(author=self.request.user)
