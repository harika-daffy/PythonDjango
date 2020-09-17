from django.db import models
from random import randint
from django.conf import settings

User=settings.AUTH_USER_MODEL
# Create your models here.
class Tweet(models.Model):
    print("............models............")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(blank=True, null=True)
    image=models.FileField(upload_to='images/',blank=True,null=True)
    
    # def __str__(self):
    #     return self.content

    class Meta:
        ordering=['-id']
        
    def serialize(self):
        return { 
        "id": self.id,
        "content": self.content,
        "likes": randint(0,200)
         }