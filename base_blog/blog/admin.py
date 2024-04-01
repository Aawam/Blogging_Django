from django.contrib import admin
from .models import Blog_Article, Categories, Tag

class Blog_ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'tag', 'author', 'date_created')

    def display_tag(self,obj):
        return ', '.join(tag.title for tag in obj.tag.all())
    display_tag.short_description = 'Tags'
    
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Blog_Article,Blog_ArticleAdmin)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Tag,TagAdmin)