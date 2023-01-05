from django.db import models


class ChatCode(models.Model):
    # Links a "chat code" to a Telegram id
    tg_user_id = models.CharField(max_length=128, unique=True)
    code = models.TextField(max_length=32, unique=True)


class Blocked(models.Model):
    # Holds the telegram id of the user blocked by another user
    blocker = models.CharField(max_length=128)
    blocked = models.CharField(max_length=128)

    class Meta:
        unique_together = ("blocker", "blocked")
