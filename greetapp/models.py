from django.db import models
from django.db.models.fields import CharField, EmailField, UUIDField

# Create your models here.

class mymodel(models.Model):
    file = models.FileField(upload_to='media')

# class UserModel(models.Model):
#      email = EmailField(max_length = 254 , blank= True , null=True)
#      status = models.BooleanField(default=False)
#      def __str__(self):
#          return self.email