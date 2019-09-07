from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class Photo(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_photos') # 연결된 객체가 지워지면 해당 하위 객체도 같이 삭제

    photo = models.ImageField(upload_to='photos/%Y/%m/%d')#,default='photos/no_image.png') # 업로드 되지 않을경우 default 값으로 대체

    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True) # auto_now_add 자동으로 값을 설정
    updated = models.DateTimeField(auto_now=True) # 객체가 수정될 때마다 자동으로 값을 설정


    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        ordering = ['-updated'] #ordering 모델의 객체들을 어떤 기준으로 정렬할 것인지 설정하는 옵션

    def get_absolute_url(self):
        return reverse('photo:photo_detail',args=[str(self.id)])

