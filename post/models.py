from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    desc = models.TextField(blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    total_comments = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 



    def __str__(self):
        return f"{self.title} | {self.user.first_name}"
    




class Post_view(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="views")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post}'


    def save(self, *args, **kwargs):
        self.post.view_count += 1
        self.post.save()
        super().save(*args, **kwargs)



class Post_comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reply_comment = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return f'{self.post}'