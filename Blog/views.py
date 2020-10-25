from django.shortcuts import render
from Blog.models import Article, Category
from django.core.paginator import Paginator

# Create your views here.

def Home(request):
    article_model = Article.objects.all()
    paginator = Paginator(article_model, 1)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'Article' : Article.objects.filter(Status='P').order_by('-Published')[:8],
        'page_obj' : page_object
    }
    return render(request, 'blog/blog.html', context)
