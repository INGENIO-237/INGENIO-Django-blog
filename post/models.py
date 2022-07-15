import datetime
from django.db import models
from django.db.models import Q
from django.utils import timezone

now = timezone.now()
au_plutard = now - datetime.timedelta(days=7)

class Category(models.Model):
    category = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category

class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    body = models.TextField()
    image = models.ImageField('Image', null=True, blank=True ,upload_to='images/')
    pub_date = models.DateField('Date posted', auto_now_add=True)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.title

    def is_archive(self):
        now = timezone.now()
        if now.year == self.pub_date.year:
            if now.month == self.pub_date.month:
                return now.day - self.pub_date.day >= 7
            else:
                return True
        else:
            return True
    
    def get_related_posts(self):
        pass

class Comment(models.Model):
    author = models.CharField(max_length=120, default='INGENIO')
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.CharField('Commentaire',max_length=300)
    pub_date = models.DateField('Date commented', auto_now_add=True)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.author + ' ' + str(self.post)

class CommentResponse(models.Model):
    comment = models.ForeignKey(Comment, related_name='responses', on_delete=models.CASCADE)
    author = models.CharField(max_length=120, default='YVES')
    body = models.CharField('Réponse', max_length=300)
    pub_date = models.DateField('Date replyed', auto_now_add=True)

    class Meta:
        ordering = ('-pk',)