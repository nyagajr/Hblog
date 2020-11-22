from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length =30)
    pic = models.ImageField(upload_to = 'articles/')
    post = models.CharField(max_length =30)
    # pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
