from django.db import models
import datetime
# Create your models here.

class Post(models.Model):
    schedule = models.TextField(null=True)
    personal_goals = models.TextField(null=True)
    professional_goals = models.TextField(null=True)
    motivation = models.TextField(null=True)
    happiness = models.TextField(null=True)
    date = models.DateField(default=datetime.date.today)
    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.date.value_to_string