from djongo import models
from djongo.models import ObjectIdField

class User(models.Model):
    _id = ObjectIdField()  # Add ObjectIdField for MongoDB compatibility
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class Meta:
        db_table = 'users'

class Team(models.Model):
    _id = ObjectIdField()  # Add ObjectIdField for MongoDB compatibility
    name = models.CharField(max_length=100)
    members = models.JSONField()  # Use JSONField to store a list of user IDs
    class Meta:
        db_table = 'teams'

class Activity(models.Model):
    _id = ObjectIdField()  # Add ObjectIdField for MongoDB compatibility
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activity'

class Leaderboard(models.Model):
    _id = ObjectIdField()  # Add ObjectIdField for MongoDB compatibility
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'

class Workout(models.Model):
    _id = ObjectIdField()  # Add ObjectIdField for MongoDB compatibility
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        db_table = 'workouts'