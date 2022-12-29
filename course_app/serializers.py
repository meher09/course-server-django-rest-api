from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import *
from django.contrib.auth import get_user_model
from django.db import IntegrityError


class CourseSerializers(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TeamSerializers(ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'


class VideoSerializers(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class ModuleSerializers(ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class MilestoneSerializers(ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'


class CustomRegisterSerializer(serializers.Serializer):

    email = serializers.CharField()
    facebook_id = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        allowed_user = AllowedUser.objects.filter(email=value).first()
        if not allowed_user:
            raise serializers.ValidationError('Email not allowed')

        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already in use')

        # Validate the associated facebook_id
        if allowed_user.facebook_id != self.context['facebook_id']:
            raise serializers.ValidationError('Invalid Facebook ID')

        return value

    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

    def create(self, validated_data, facebook_id):
        allowed_user = AllowedUser.objects.filter(
            facebook_id=facebook_id).first()
        if not allowed_user:
            raise serializers.ValidationError('Facebook ID not allowed')

        User = get_user_model()
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.create_user(
            email=email,
            password=password,
            username=email,  # Set the username as the email
        )
        return user
