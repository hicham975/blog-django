from django.apps import AppConfig

class CategoriesConfig(AppConfig):
    name = 'categories'

class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'posts'
