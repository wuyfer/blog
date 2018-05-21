from django.db import models
from django.core.paginator import Paginator
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20,unique=True)
    def __unicode__(self):
        return u'%s'%self.name
    def __str__(self):
        return u'%s'%self.name
class Tag(models.Model):
    name=models.CharField(max_length=20,unique=True)
    def __unicode__(self):
        return u'%s'%self.name
    def __str__(self):
        return u'%s'%self.name
class Post(models.Model):
    title=models.CharField(max_length=20)
    desc=RichTextUploadingField()
    content=models.TextField()
    created=models.DateField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,)
    tags=models.ManyToManyField(Tag)
    def __unicode__(self):
        return u'%s'%self.title
    def __str__(self):
        return u'%s'%self.title
    @staticmethod
    def get_posts_by_page(num,per_page=1):
        num=int(num)
        paginator=Paginator(Post.objects.order_by('-modified').all(),per_page)
        if num<1:
            num=1
        if num>paginator.num_pages:
            num=paginator.num_pages
        page=paginator.page(num)

        previous=2
        next=2
        if num<=previous:
            start=1
            end=start+previous+next
        if num>previous:
            start=num-previous
            end=num+next
        if end>paginator.num_pages:
            end=paginator.num_pages

        return (page,range(start,end+1))
