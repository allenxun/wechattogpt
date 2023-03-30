from django.db import models

# Create your models here.
class message_data(models.Model):
    ToUserName = models.CharField(max_length=100)
    FromUserName = models.CharField(max_length=100)
    CreateTime = models.CharField(max_length=100)
    MsgType = models.CharField(max_length=100)
    Content = models.CharField(max_length=1500)
    MsgId = models.CharField(max_length=100)
    MsgDataId = models.CharField(max_length=100)
    Idx = models.CharField(max_length=100)

    def __str__(self):
        return self.ToUserName
