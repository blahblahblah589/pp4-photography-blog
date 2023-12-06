from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.conf import settings

STATUS = ((False, 'Draft'), (True, 'Published'))

class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = CloudinaryField('image')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photo_post')
    caption = models.TextField()
    location = models.TextField()
    likes = models.ManyToManyField(User, related_name='photo_likes', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(choices=STATUS, default=False)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='photo_comment')
    comment_content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f'{self.comment_content} from {self.created_by}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def user_points(user_id):
        user = User.objects.get(id=user_id)
        posts_amount = Post.objects.filter(created_by=user).count()
        comments_amount = Comment.objects.filter(created_by=user).count()
        points = (posts_amount * 100) + (comment_amount * 50)

        return points
