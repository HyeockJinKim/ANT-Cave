from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class UserInfo(models.Model):
    """
    User:
        username: 아이디
        password: 비밀번호
        email: 이메일
        first_name:
        last_name:
        groups
        user_permissions
        is_staff
        is_active
        is_superuser
        last_login
        date_joined
    user_num:
    user_phone:
    level:
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=10)
    user_num = models.IntegerField()
    user_phone = models.CharField(max_length=20)
    is_attend = models.CharField(max_length=1)
    level = models.PositiveSmallIntegerField(default=0)
    signup_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_name.encode('utf8')


class Label(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)


class TeamPost(models.Model):
    post_num = models.AutoField(primary_key=True)
    parent = models.IntegerField()
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)


class TeamComment(models.Model):
    comment_num = models.AutoField(primary_key=True)
    parent = models.IntegerField()
    post = models.ForeignKey(TeamPost, primary_key=True, on_delete=models.CASCADE)
    text = models.TextField()


class TeamLabel(models.Model):
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    post = models.ForeignKey(TeamPost, on_delete=models.CASCADE)


class TeamPostFile(models.Model):
    post = models.ForeignKey(TeamPost, on_delete=models.CASCADE)
    file = models.FileField()
