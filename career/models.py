from django.db import models
from users.models import User
from assessments.models import Skill

class Career(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    required_skills = models.ManyToManyField(Skill)  # Skills needed for this career
    difficulty_level = models.CharField(max_length=50)  # beginner/intermediate/expert

    def __str__(self):
        return self.name


class CareerRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    recommended_on = models.DateTimeField(auto_now_add=True)
    score_match = models.FloatField(default=0)  # match percentage by AI (0–100)

    def __str__(self):
        return f"{self.user.username} → {self.career.name}"
