from django.urls import path
from Blog.views import Home, category_of_site, Post

app_name = 'blog'

urlpatterns = [
    path('', Home, name='home_url'),
    path('Article/<str:Post_Slug>', Post, name='Post_url'),
    path('category/<str:Category_Slug>', category_of_site, name='Category_url' )
]
