from django.db import models
from users.models import User

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100)  # e.g. "Programming", "Soft Skill"

    def __str__(self):
        return self.name


class Assessment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.ManyToManyField(Skill)  # Skills this assessment evaluates
    total_marks = models.IntegerField(default=100)

    def __str__(self):
        return self.title


class Question(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1)  # "A/B/C/D"

    def __str__(self):
        return self.text[:50]


class UserAssessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)
    skill_scores = models.JSONField(default=dict)  # {"python": 70, "logical": 80}

    def __str__(self):
        return f"{self.user.username} - {self.assessment.title}"
