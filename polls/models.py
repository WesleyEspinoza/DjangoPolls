"""temp Doc String"""
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    """temp Doc String"""
    def __str__(self):
        """temp Doc String"""
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        """temp Doc String"""
        return self.pub_date >= timezone.now() - timezone.datetime.timedelta(days=1)

class Choice(models.Model):
    """temp Doc String"""
    def __str__(self):
        """temp Doc String"""
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
