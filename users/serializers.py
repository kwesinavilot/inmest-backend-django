from rest_framework import serializers
from .models import IMUser, Cohort, CohortMember

class UserSerializers(serializers.Serializer):
    id = serializers.IntergerField()

class IMUserSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField()
        first_name = serializers.CharField(max_length=255)
        last_name = serializers.CharField(max_length=255)
        is_active = serializers.BooleanField(default=True)
        user_type = serializers.ChoiceField(choices=IMUser.USER_TYPE_CHOICES, default='EIT')
        date_created = serializers.DateTimeField()

class CohortSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField()
        name = serializers.CharField(max_length=255)
        description = serializers.CharField(allow_blank=True)
        year = serializers.IntegerField()
        start_date = serializers.DateField()
        end_date = serializers.DateField()
        is_active = serializers.BooleanField(default=True)
        date_created = serializers.DateTimeField()
        date_modified = serializers.DateTimeField()
        author = IMUserSerializer()

class CohortMemberSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField()
        cohort = CohortSerializer()
        member = IMUserSerializer()
        is_active = serializers.BooleanField(default=True)
        date_created = serializers.DateTimeField()
        date_modified = serializers.DateTimeField()
        author = IMUserSerializer()
