from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField("Date Published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
