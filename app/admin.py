from django.contrib import admin
from .models import Article, Category, BlogComment, Tag

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display=("title","body","created_time",)
	
class BlogCommentAdmin(admin.ModelAdmin):
    list_display =("user_name", "body","created_time")

admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register([Category, Tag])