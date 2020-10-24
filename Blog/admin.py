from django.contrib import admin
from Blog.models import Article, Category

# Register your models here.
class Category_Admin(admin.ModelAdmin):
    list_display = ('Position', 'Status', 'Published')
    list_filter = (['Status'])
    search_fields = ('Title', 'Slug')
    prepopulated_fields = {'Slug':('Title',)}

admin.site.register(Category, Category_Admin)

class Article_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Status', 'Published')
    list_filter = ('Published', 'Status')
    search_fields = ('Title', 'Slug', 'Descraption')
    prepopulated_fields = {'Slug':('Title',)}

admin.site.register(Article, Article_Admin)
