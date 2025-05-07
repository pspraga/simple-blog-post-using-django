from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    tags = models.CharField(max_length=255, help_text='Comma-separated tags')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
