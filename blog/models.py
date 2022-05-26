from django.db import models
from django.utils import timezone
# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/blog<id>/<filename>
    return 'blog/{0}/{1}'.format(instance.user.id, filename)


class Post(models.Model):

    class PostObjects:
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.Charfield(max_length=250)
    thumbnail = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    excerpt = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=250,unique_for_date='published',null=False, unique=True)
    published = models.DatetimeField(default=timezone.now)
    author = models.ForeignKey('User', on_delete=models.CASCADE , related_name='post_user')
    
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()
    postObjects = PostObjects()

    class Meta:
        ordering = ('-published',)
    def __str__(self):
        return self.title

