from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Day(models.Model):
    user = models.ForeignKey(User, related_name='day', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.start_time.strftime("%Y-%m-%d %H:%M:%S")

class Activity(models.Model):
    day = models.ForeignKey(Day, related_name='activity', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now_add=True)
    exercise = models.CharField(max_length=30)
    structure = models.CharField(max_length=30)

    def __str__(self):
        return self.exercise

class Set(models.Model):
    activity = models.ForeignKey(Activity, related_name='set', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now_add=True)
    set_number = models.IntegerField()
    goal_weight = models.DecimalField(decimal_places=2, max_digits=10)
    weight = models.DecimalField(decimal_places=2, max_digits=10)
    goal_reps = models.DecimalField(decimal_places=2, max_digits=10)
    reps = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return "set " + str(self.set_number)
