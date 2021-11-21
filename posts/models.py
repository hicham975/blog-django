from django.db import models
from autoslug import AutoSlugField
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model




class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = True, null=True)
    title = models.CharField(max_length=100) 
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of

        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "Add categories"     

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])  


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True, null=False, editable=False)
    def __str__(self):
        return self.name
    class Meta:
  
        verbose_name_plural = "Add tag"    


# Create your models here.
class Posts(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=250) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False)
    intro = RichTextField()
    image = models.ImageField(upload_to='images/')
    post = RichTextField() 
    is_published = models.BooleanField(default=False, verbose_name="Publish")
    is_featured = models.BooleanField(default=False, verbose_name="Feature")       
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)
    editeur = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def __str__(self):
        return self.title 
    def image_tag(self):
    	return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))

    class Meta:
  
        verbose_name_plural = "Add post"    