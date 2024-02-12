from django.db import models
from django.contrib.auth.models import User  # Assuming custom user management later

# Create your models here.
class IMUser(models.Model):
    USER_TYPE_CHOICES = (
        ('EIT', 'EIT'),
        ('TEACHING_FELLOW', 'Teaching Fellow'),
        ('ADMIN_STAFF', 'Admin Staff'),
        ('ADMIN', 'Admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='im_user')  # Link to Django's User model
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='EIT')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user_type})"

class Cohort(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, related_name='authored_cohorts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.year})"

class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, related_name='members', on_delete=models.CASCADE)
    member = models.ForeignKey(IMUser, related_name='cohorts', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, related_name='added_cohort_members', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member.username} in {self.cohort.name}"
