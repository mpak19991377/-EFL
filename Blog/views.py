from django.shortcuts import render
from Blog.models import Article, Category

# Create your views here.
def Home(request):
    context = {
        'Article' : Article.objects.filter(Status='P')
    }
    return render(request, 'blog/blog.html', context)