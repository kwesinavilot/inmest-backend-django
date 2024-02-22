from rest_framework import serializers
from .models import Course, ClassSchedule, ClassAttendance, Query, QueryComment

class CourseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=1000)
    description = serializers.TextField(default ="N/A", allow_blank=True, allow_null=True)
    date_created = serializers.DateTimeField()
    date_modified = serializers.DateTimeField()

class ClassScheduleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    description = serializers.TextField(allow_blank=True)
    start_date_and_time = serializers.DateTimeField()
    end_date_and_time = serializers.DateTimeField()
    is_repeated = serializers.BooleanField(default=False)
    repeat_frequency = serializers.CharField(max_length=10, allow_blank=True, allow_null=True)
    is_active = serializers.BooleanField()
    organizer = serializers.PrimaryKeyRelatedField(read_only=True)
    cohort = serializers.PrimaryKeyRelatedField(read_only=True)
    venue = serializers.CharField(max_length=255, allow_blank=True)

class ClassAttendanceSerializer(serializers.ModelSerializer):
    class_schedule = serializers.PrimaryKeyRelatedField(read_only=True)
    attendee = serializers.PrimaryKeyRelatedField(read_only=True)
    is_present = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    date_modified = serializers.DateTimeField()
    author = serializers.PrimaryKeyRelatedField(read_only=True)

class QuerySerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    description = serializers.TextField(allow_blank=True)
    submitted_by = serializers.PrimaryKeyRelatedField(read_only=True)
    assigned_to = serializers.PrimaryKeyRelatedField(read_only=True, allow_null=True)
    resolution_status = serializers.CharField(max_length=20)
    date_created = serializers.DateTimeField()
    date_modified = serializers.DateTimeField()
    author = serializers.PrimaryKeyRelatedField(read_only=True)

class QueryCommentSerializer(serializers.ModelSerializer):
    query = serializers.PrimaryKeyRelatedField(read_only=True)
    comment = serializers.TextField()
    date_created = serializers.DateTimeField()
    date_modified = serializers.DateTimeField()
    author = serializers.PrimaryKeyRelatedField(read_only=True)
