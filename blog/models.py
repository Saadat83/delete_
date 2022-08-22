from django.db import models
from django.db.models import Model
from django.utils import timezone
from django.urls import reverse

class Post(Model):
    tittle = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    post_date = models.DateField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to ='post_image/')

    def __str__(self):
        return f'tittle: {self.tittle}, author: {self.author}'

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})