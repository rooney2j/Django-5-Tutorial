import datetime

from django.db import models
from django.utils import timezone

from django.contrib import admin

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


    def __str__(self) -> str:
        return self.question_text
    

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()    # datetime.datetime(2024, 5, 27, ...)
        one_day_ago = now - datetime.timedelta(days=1)
        is_recent = (one_day_ago <= self.pub_date) and (self.pub_date <= now)

        return is_recent


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.choice_text