from django.db import models

# Create your models here.
class Question(models.Model):
    q_text = models.CharField(max_length = 200)
    participants = models.IntegerField(default = 0)

    def __str__(self):
        return self.q_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    c_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    percentage = models.FloatField(default = 0)

    def __str__(self):
        return self.c_text