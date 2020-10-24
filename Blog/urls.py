from django.urls import path
from Blog.views import Home

app_name = 'blog'

urlpatterns = [
    path('', Home, name='home_url')
]
