from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')
        


class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title= models.CharField(max_length=56)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    category=models.CharField(max_length=56,default=True)
    author=models.ForeignKey(User,related_name='blog_post',on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='image/',default="") 
    body=RichTextField(blank=True,null=True)
    publish=models.DateTimeField(default=timezone.now)
    created= models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='published')
    objects=CustomManager()
    tags=TaggableManager()

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])
    

#adding comments model here.

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=32)
    email =models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    
    class Meta:
       ordering=('-created',)

    def __str__(self):
        return 'Commented By{} on {}'.format(self.name,self.post)



class Contactus(models.Model):
    Name=models.CharField(max_length=32)
    Email=models.EmailField()
    Mobile=models.IntegerField()
    Feedback=models.TextField()
    Time=models.DateTimeField(auto_now_add=True)





        

