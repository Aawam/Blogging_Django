from django.contrib import admin
from .models import Blog_Article, Category, Tag

# Register your models here.

class Blog_ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created', 'display_categories', 'display_tags')    
    
    def display_tags(self, obj):
        return ', '.join(tag.title for tag in obj.tags.all())
    display_tags.short_description = 'Tags'

    def display_categories(self, obj):
        return obj.categories.title if obj.categories else "No category"
    display_categories.short_description = 'Categories'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Blog_Article,Blog_ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)