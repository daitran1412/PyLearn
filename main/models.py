from django.db import models

# Create your models here.

class Passed(models.Model):
    # user_id, problem
    user_id = models.IntegerField()
    problem_id = models.IntegerField()
