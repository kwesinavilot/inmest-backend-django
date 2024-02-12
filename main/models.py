from django.db import models
from django.contrib.auth.models import User  # Assuming IMUser inherits from User
from users.models import Cohort

class Course(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(default ="N/A", blank = True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank = True, null=True)
    date_modified = models.DateTimeField(auto_now=True,  blank = True, null=True)

    def __str__(self):
        return f'{self.name}'
    
class ClassSchedule(models.Model):
    REPEAT_FREQUENCY_CHOICES = (
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
        ('YEARLY', 'Yearly'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default=False)
    repeat_frequency = models.CharField(max_length=10, choices=REPEAT_FREQUENCY_CHOICES, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_classes')
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='class_schedules')
    venue = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.title} ({self.start_date_and_time})'

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, related_name='attendances')
    attendee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='class_attendances')
    is_present = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendance_authored')

    def __str__(self):
        return f'{self.attendee.username} - {self.class_schedule.title}'

class Query(models.Model):
    RESOLUTION_STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('DECLINED', 'Declined'),
        ('RESOLVED', 'Resolved'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submitted_queries')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_queries', blank=True, null=True)
    resolution_status = models.CharField(max_length=20, choices=RESOLUTION_STATUS_CHOICES, default='PENDING')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='query_authored')

    def __str__(self):
        return f'{self.title} - {self.submitted_by.username}'

class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='query_comments')

    def __str__(self):
        return f'{self.query.title} - {self.author.username}'