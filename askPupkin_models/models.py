from django.db import models
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from .managers import *


class Profile(models.Model):
    nickname = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='./static/avs', blank=True)
    reg_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    

class Tag(models.Model):
    name = models.CharField(max_length=10, unique=True, validators=[
        validators.RegexValidator(
            "[a-z]{2,10}",
            "Tag is not a correct!"
        )
    ])


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    class Meta:
        unique_together = ('user', 'content_type', 'object_id',)


class Question(models.Model):
    objects = QuestionsQueryset().as_manager()
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    likes = GenericRelation(Like)
    class Meta:
        ordering = ['-creation_date']


class Answer(models.Model):
    objects = AnswersManager()
    content = models.TextField()
    correctness = models.BooleanField(default=False)
    creation_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    likes = GenericRelation(Like)