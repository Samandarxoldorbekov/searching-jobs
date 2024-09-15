from django.db import models


class TermChoise(models.TextChoices):
    LONGTIME = "long", "LongTime"
    ONETIME = "onetime", "OneTime"

class JobsType(models.TextChoices):
    ONLINE = "online", "online"
    OFLINE = "ofline", "ofline"

class DegreeChoise(models.TextChoices):
    INAPET = "tajribasiz", "Tajribasiz"
    EXPET = "tajribali", "Tajribali"

class DiplomChoise(models.TextChoices):
    NOTNO = "muhum emas", "Muhum emas"
    BACHALA ="bakalavir", "Bakalavir"
    MAGESTER ="magistir", "Magister"


class Social(models.Model):
    class SocilMediaChoices(models.TextChoices):
        TELEGRAM = "telegram","Telegram"
        INSTAGRAM = "instagram","Instagram"
        FACEBOOK = "facebook", "Facebook"
        YOUTUBE = "youtube", "Youtube"
    title = models.CharField(max_length=255)
    social = models.CharField(choices=SocilMediaChoices.choices,max_length=16)
    link = models.URLField()

    def __str__(self) -> str:
        return self.title


class Region(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title