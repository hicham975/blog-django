from django.contrib import admin
from .models import *
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','slug')

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title','slug','image_tag')

admin.site.register(Posts,PostsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)

