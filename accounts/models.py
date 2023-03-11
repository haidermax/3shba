from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
   user_id = models.OneToOneField(User, on_delete=models.CASCADE)
   phone = models.BigIntegerField(verbose_name='رقم الهاتف')
   img = models.ImageField(upload_to='media/usrimg/', default='media/usrimg/default.png', verbose_name='الصورة')

   def __str__(self):
      return self.user_id.username
      

