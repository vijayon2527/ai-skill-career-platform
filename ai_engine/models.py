from django.db import models
from users.models import User
from assessments.models import Assessment

class AIScoreHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.SET_NULL, null=True)
    raw_scores = models.JSONField(default=dict)  # All question-level scores
    normalized_scores = models.JSONField(default=dict)  # After AI scaling
    ai_summary = models.TextField()  # "Your Python logic is strong..."
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AI Score - {self.user.username}"
