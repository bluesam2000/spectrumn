from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField
from cropperjs.models import CropperImageField

from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Category(models.Model):
    id_of_cat=models.AutoField
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cat-posts', kwargs={'id': self.pk})


class Post(models.Model):
    id_of_post=models.AutoField
    title=models.CharField(max_length=100)
  #  content=models.TextField()
    content= RichTextUploadingField()
    date_posted=models.DateTimeField(default=timezone.now())
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    #thumbnail=CropperImageField(upload_to='post_images')
    thumbnail=models.ImageField(upload_to='post_images')
    likes=models.ManyToManyField(User,related_name='posts_like',default=None)
    dislikes=models.ManyToManyField(User,related_name='posts_dislike',default=None)
    #featured=models.BooleanField()


    def __str__(self):
        return self.title

    def number_of_likes(self): # this is the function that we are gonna call
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()


    def get_absolute_url(self):
        return reverse('post-details',kwargs={'id':self.pk})

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

    @property
    def get_comments(self):
        return self.comments.all()  # this is from related name is comment



    #
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     thumbnail=Image.open(self.thumbnail.path)
    #     if thumbnail.height > 300 or thumbnail.width > 300 :
    #         output_size=(200,200)
    #         thumbnail.thumbnail(output_size)
    #         thumbnail.save(self.thumbnail.path)
    #    # img_1=Image.open(self.blog_image.path)
    #     img_2=Image.open(self.blog_image_1.path)
    #     #
    #     #
    #     # if img_1.height > 400 or img_1.width > 400 or img_2.height > 400 or img_2.width > 400 :
    #     #     output_size=(400,400)
    #     #     img_1.thumbnail(output_size)
    #     #     img_2.thumbnail(output_size)
    #     #     img_1.save(self.blog_image.path)
    #     #     img_2.save(self.blog_image_1.path)
    #

class PostView(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)   # @property

    def __str__(self):
        return self.user.username
