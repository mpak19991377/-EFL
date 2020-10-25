from django.urls import path
from Blog.views import Home, category_of_site

app_name = 'blog'

urlpatterns = [
    path('', Home, name='home_url'),
    path('category/<str:Slug>', category_of_site, name='Category_url' )
]
