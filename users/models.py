from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPES = (
        ("student", "Student"),
        ("professional", "Professional"),
        ("admin", "Admin"),
    )

    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default="student")

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username



class SkillProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="skill_profile")

    overall_score = models.FloatField(default=0)
    skill_strengths = models.JSONField(default=dict)  
    # Example: {"python": 80, "ml": 60}

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} Profile"
