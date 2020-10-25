from django.contrib import admin
from Blog.models import Article, Category

# Register your models here.
class Category_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Position',  'Status', 'Published')
    list_filter = (['Status'])
    search_fields = ('Title', 'Slug')
    prepopulated_fields = {'Slug':('Title',)}

admin.site.register(Category, Category_Admin)

class Article_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Categorys', 'Status', 'Published')
    list_filter = ('Published', 'Status')
    search_fields = ('Title', 'Slug', 'Descraption')
    prepopulated_fields = {'Slug':('Title',)}

    def Categorys(self, obj):
        return " ,".join([Category.Title for Category in obj.Category.all()])
        

admin.site.register(Article, Article_Admin)
