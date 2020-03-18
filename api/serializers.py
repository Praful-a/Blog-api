from rest_framework import serializers
from account.models import Account
from post.models import BlogPost


class UserProfileSerializer(serializers.ModelSerializer):
    """A Serializer for our user profile objects."""
    class Meta:
        model = Account
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""
        user = Account(
            email=validated_data['email'],
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class BlogPostSerializer(serializers.ModelSerializer):
    """A Serializer for blog post item."""
    class Meta:

        model = BlogPost
        fields = ('id', 'author', 'title', 'body', 'image', 'slug')
        # fields = ['title', 'body', 'image', 'date_updated', 'username']
        extra_kwargs = {'author': {'read_only': True}}
