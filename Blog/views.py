from django.shortcuts import render
from Blog.models import Article, Category
from django.core.paginator import Paginator

# Create your views here.

def Home(request):
    article_model = Article.objects.all()
    paginator = Paginator(article_model, 8)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'Article' : Article.objects.filter(Status='P').order_by('-Published')[:8],
        'Article_2' : Article.objects.filter(Status='P').order_by('-Published')[:4],
        'Category' : Category.objects.filter(Status= True),
        'page_obj' : page_object,
    }
    return render(request, 'blog/blog.html', context)
