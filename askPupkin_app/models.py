from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .managers import QuestionsManager

class Profile(models.Model):
    nickname = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='./static/avs', blank=True)
    reg_date = models.DateField(default=datetime.now().date())
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Tag(models.Model):
    name = models.CharField(max_length=15, unique=True)

class Question(models.Model):
    objects = QuestionsManager()
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    creation_date = models.DateField(default=datetime.now().date())
    rating = models.IntegerField()
    viewed = models.IntegerField(default=0)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rated = models.ManyToManyField(User)
    tags = models.ManyToManyField(Tag)

class Answer(models.Model):
    content = models.TextField()
    correctness = models.BooleanField(default=False)
    creation_date = models.DateField(default=datetime.now().date())
    rating = models.IntegerField()
    rated = models.ManyToManyField(User)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
